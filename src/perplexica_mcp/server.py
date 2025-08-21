"""Perplexica MCP Server implementation."""

import asyncio
import json
import os
from typing import Any, Dict, List, Optional, Sequence, Union

import httpx
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    ListToolsRequest,
    ListToolsResult,
    TextContent,
    Tool,
)
from pydantic import BaseModel, Field


class ChatModel(BaseModel):
    """Chat model configuration."""

    provider: str
    name: str
    customOpenAIBaseURL: Optional[str] = None
    customOpenAIKey: Optional[str] = None


class EmbeddingModel(BaseModel):
    """Embedding model configuration."""

    provider: str
    name: str


class SearchRequest(BaseModel):
    """Perplexica search request."""

    chatModel: Optional[ChatModel] = None
    embeddingModel: Optional[EmbeddingModel] = None
    optimizationMode: Optional[str] = Field(
        default="balanced", description="speed, balanced"
    )
    focusMode: str = Field(
        description="webSearch, academicSearch, writingAssistant, wolframAlphaSearch, youtubeSearch, redditSearch"
    )
    query: str
    history: Optional[List[List[str]]] = None
    systemInstructions: Optional[str] = None
    stream: bool = False


class SearchSource(BaseModel):
    """Search result source."""

    pageContent: str
    metadata: Dict[str, Any]


class SearchResponse(BaseModel):
    """Perplexica search response."""

    message: str
    sources: List[SearchSource]


class PerplexicaClient:
    """Client for interacting with Perplexica API."""

    def __init__(self, base_url: str = "http://localhost:3000"):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=60.0)

    async def search(self, request: SearchRequest) -> SearchResponse:
        """Perform a search using Perplexica."""
        url = f"{self.base_url}/api/search"

        try:
            response = await self.client.post(
                url,
                json=request.model_dump(exclude_none=True),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()

            data = response.json()
            return SearchResponse(**data)

        except httpx.HTTPError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode JSON response: {e}")
        except Exception as e:
            raise Exception(f"Search failed: {e}")

    async def get_models(self) -> Dict[str, str]:
        """Get available models from Perplexica."""
        url = f"{self.base_url}/api/models"

        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode JSON response: {e}")
        except Exception as e:
            raise Exception(f"Failed to get models: {e}")

    async def close(self) -> None:
        """Close the HTTP client."""
        await self.client.aclose()


class PerplexicaServer:
    """Perplexica MCP Server."""

    def __init__(self):
        self.server = Server("perplexica")
        base_url = os.getenv("PERPLEXICA_BASE_URL", "http://localhost:3000")
        self.client = PerplexicaClient(base_url)

        # Register handlers
        self.server.list_tools = self.list_tools
        self.server.call_tool = self.call_tool

    async def list_tools(self, request: ListToolsRequest) -> ListToolsResult:
        """List available tools."""
        return ListToolsResult(
            tools=[
                Tool(
                    name="perplexica_search",
                    description="Perform AI-powered search using Perplexica with various focus modes",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query",
                            },
                            "focusMode": {
                                "type": "string",
                                "enum": [
                                    "webSearch",
                                    "academicSearch",
                                    "writingAssistant",
                                    "wolframAlphaSearch",
                                    "youtubeSearch",
                                    "redditSearch",
                                ],
                                "description": "The focus mode for the search",
                                "default": "webSearch",
                            },
                            "optimizationMode": {
                                "type": "string",
                                "enum": ["speed", "balanced"],
                                "description": "Optimization mode for the search",
                                "default": "balanced",
                            },
                            "chatModel": {
                                "type": "object",
                                "properties": {
                                    "provider": {"type": "string"},
                                    "name": {"type": "string"},
                                    "customOpenAIBaseURL": {"type": "string"},
                                    "customOpenAIKey": {"type": "string"},
                                },
                                "required": ["provider", "name"],
                                "description": "Chat model configuration",
                            },
                            "embeddingModel": {
                                "type": "object",
                                "properties": {
                                    "provider": {"type": "string"},
                                    "name": {"type": "string"},
                                },
                                "required": ["provider", "name"],
                                "description": "Embedding model configuration",
                            },
                            "history": {
                                "type": "array",
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "minItems": 2,
                                    "maxItems": 2,
                                },
                                "description": "Conversation history as [role, message] pairs",
                            },
                            "systemInstructions": {
                                "type": "string",
                                "description": "Custom system instructions to guide the AI's response",
                            },
                            "stream": {
                                "type": "boolean",
                                "description": "Enable streaming responses",
                                "default": False,
                            },
                        },
                        "required": ["query"],
                    },
                ),
                Tool(
                    name="perplexica_get_models",
                    description="Get available chat and embedding models from Perplexica",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
            ]
        )

    async def call_tool(self, request: CallToolRequest) -> CallToolResult:
        """Handle tool calls."""
        try:
            if request.params.name == "perplexica_search":
                return await self._handle_search(request.params.arguments or {})
            elif request.params.name == "perplexica_get_models":
                return await self._handle_get_models()
            else:
                raise ValueError(f"Unknown tool: {request.params.name}")

        except Exception as e:
            return CallToolResult(
                content=[TextContent(type="text", text=f"Error: {str(e)}")],
                isError=True,
            )

    async def _handle_search(self, arguments: Dict[str, Any]) -> CallToolResult:
        """Handle search requests."""
        # Extract and validate arguments
        query = arguments.get("query")
        if not query:
            raise ValueError("Query is required")

        focus_mode = arguments.get("focusMode", "webSearch")
        optimization_mode = arguments.get("optimizationMode", "balanced")

        # Build search request
        search_request = SearchRequest(
            query=query,
            focusMode=focus_mode,
            optimizationMode=optimization_mode,
            stream=arguments.get("stream", False),
        )

        # Add optional models
        if "chatModel" in arguments:
            chat_model_data = arguments["chatModel"]
            search_request.chatModel = ChatModel(**chat_model_data)

        if "embeddingModel" in arguments:
            embedding_model_data = arguments["embeddingModel"]
            search_request.embeddingModel = EmbeddingModel(**embedding_model_data)

        # Add optional fields
        if "history" in arguments:
            search_request.history = arguments["history"]

        if "systemInstructions" in arguments:
            search_request.systemInstructions = arguments["systemInstructions"]

        # Perform search
        result = await self.client.search(search_request)

        # Format response
        response_text = f"**Search Results for:** {query}\n\n"
        response_text += f"**Focus Mode:** {focus_mode}\n\n"
        response_text += f"**Answer:**\n{result.message}\n\n"

        if result.sources:
            response_text += "**Sources:**\n"
            for i, source in enumerate(result.sources, 1):
                title = source.metadata.get("title", "Unknown Title")
                url = source.metadata.get("url", "")
                response_text += f"{i}. [{title}]({url})\n"
                if source.pageContent:
                    # Truncate long content
                    content = (
                        source.pageContent[:200] + "..."
                        if len(source.pageContent) > 200
                        else source.pageContent
                    )
                    response_text += f"   {content}\n\n"

        return CallToolResult(content=[TextContent(type="text", text=response_text)])

    async def _handle_get_models(self) -> CallToolResult:
        """Handle get models requests."""
        models = await self.client.get_models()

        response_text = "**Available Models:**\n\n"

        # Format chat models
        if "chatModels" in models:
            response_text += "**Chat Models:**\n"
            for provider, provider_models in models["chatModels"].items():
                response_text += f"\n*{provider}:*\n"
                for model_key, model_info in provider_models.items():
                    display_name = model_info.get("displayName", model_key)
                    response_text += f"- `{model_key}`: {display_name}\n"

        # Format embedding models
        if "embeddingModels" in models:
            response_text += "\n**Embedding Models:**\n"
            for provider, provider_models in models["embeddingModels"].items():
                response_text += f"\n*{provider}:*\n"
                for model_key, model_info in provider_models.items():
                    display_name = model_info.get("displayName", model_key)
                    response_text += f"- `{model_key}`: {display_name}\n"

        return CallToolResult(content=[TextContent(type="text", text=response_text)])

    async def run(self) -> None:
        """Run the server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="perplexica",
                    server_version="0.1.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=None, experimental_capabilities=None
                    ),
                ),
            )

    async def cleanup(self) -> None:
        """Cleanup resources."""
        await self.client.close()


async def main() -> None:
    """Main entry point."""
    server = PerplexicaServer()
    try:
        await server.run()
    finally:
        await server.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
