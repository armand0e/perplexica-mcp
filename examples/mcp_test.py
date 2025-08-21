"""Test script to demonstrate MCP server functionality."""

import asyncio
import json
from mcp.types import CallToolRequest, CallToolRequestParams
from perplexica_mcp.server import PerplexicaServer


async def test_mcp_server():
    """Test the MCP server tools."""
    server = PerplexicaServer()

    print("Testing Perplexica MCP Server")
    print("=" * 40)

    # Test list_tools
    print("\n1. Testing list_tools...")
    tools_result = await server.list_tools(None)
    print(f"Available tools: {len(tools_result.tools)}")
    for tool in tools_result.tools:
        print(f"  - {tool.name}: {tool.description}")

    # Test get_models (this will fail without a running Perplexica instance)
    print("\n2. Testing perplexica_get_models...")
    try:
        models_request = CallToolRequest(
            method="tools/call",
            params=CallToolRequestParams(name="perplexica_get_models", arguments={}),
        )
        models_result = await server.call_tool(models_request)
        if models_result.isError:
            print(
                f"Expected error (no Perplexica instance): {models_result.content[0].text}"
            )
        else:
            print("Models retrieved successfully!")
    except Exception as e:
        print(f"Expected error (no Perplexica instance): {e}")

    # Test search (this will also fail without a running Perplexica instance)
    print("\n3. Testing perplexica_search...")
    try:
        search_request = CallToolRequest(
            method="tools/call",
            params=CallToolRequestParams(
                name="perplexica_search",
                arguments={
                    "query": "What is artificial intelligence?",
                    "focusMode": "webSearch",
                    "optimizationMode": "balanced",
                },
            ),
        )
        search_result = await server.call_tool(search_request)
        if search_result.isError:
            print(
                f"Expected error (no Perplexica instance): {search_result.content[0].text}"
            )
        else:
            print("Search completed successfully!")
            print(f"Result: {search_result.content[0].text[:200]}...")
    except Exception as e:
        print(f"Expected error (no Perplexica instance): {e}")

    # Test invalid tool
    print("\n4. Testing invalid tool...")
    try:
        invalid_request = CallToolRequest(
            method="tools/call",
            params=CallToolRequestParams(name="invalid_tool", arguments={}),
        )
        invalid_result = await server.call_tool(invalid_request)
        print(f"Error result: {invalid_result.content[0].text}")
    except Exception as e:
        print(f"Error: {e}")

    await server.cleanup()
    print("\nMCP server test completed!")


if __name__ == "__main__":
    asyncio.run(test_mcp_server())
