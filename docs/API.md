# Perplexica MCP Server API Documentation

## Overview

The Perplexica MCP Server provides tools to interact with a local Perplexica instance through the Model Context Protocol (MCP). This allows AI assistants like Claude to perform AI-powered searches using your local Perplexica installation.

## Tools

### perplexica_search

Perform AI-powered searches with various focus modes.

#### Parameters

- **query** (string, required): The search query
- **focusMode** (string, optional): The focus mode for the search
  - `webSearch` (default): General web search
  - `academicSearch`: Academic and research-focused search
  - `writingAssistant`: Writing and content creation assistance
  - `wolframAlphaSearch`: Mathematical and computational queries
  - `youtubeSearch`: YouTube video search
  - `redditSearch`: Reddit discussion search
- **optimizationMode** (string, optional): Optimization mode
  - `balanced` (default): Balanced speed and quality
  - `speed`: Prioritize speed
- **chatModel** (object, optional): Chat model configuration
  - `provider` (string): Model provider (e.g., "openai", "ollama")
  - `name` (string): Model name (e.g., "gpt-4o-mini")
  - `customOpenAIBaseURL` (string, optional): Custom OpenAI base URL
  - `customOpenAIKey` (string, optional): Custom OpenAI API key
- **embeddingModel** (object, optional): Embedding model configuration
  - `provider` (string): Model provider
  - `name` (string): Model name
- **history** (array, optional): Conversation history as [role, message] pairs
- **systemInstructions** (string, optional): Custom instructions to guide the AI
- **stream** (boolean, optional): Enable streaming responses (default: false)

#### Example Usage

```json
{
  "query": "What are the latest developments in quantum computing?",
  "focusMode": "academicSearch",
  "optimizationMode": "balanced",
  "chatModel": {
    "provider": "openai",
    "name": "gpt-4o-mini"
  },
  "systemInstructions": "Focus on recent breakthroughs and practical applications"
}
```

#### Response

Returns a formatted text response containing:
- The search query and focus mode used
- The AI-generated answer
- List of sources with titles, URLs, and content snippets

### perplexica_get_models

Get available chat and embedding models from the Perplexica instance.

#### Parameters

None.

#### Response

Returns a formatted list of available models organized by provider, including both chat models and embedding models.

## Configuration

### Environment Variables

- **PERPLEXICA_BASE_URL**: Base URL of the Perplexica instance (default: "http://localhost:3000")

### Claude Desktop Configuration

Add to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "perplexica": {
      "command": "python",
      "args": ["-m", "perplexica_mcp"],
      "env": {
        "PERPLEXICA_BASE_URL": "http://localhost:3000"
      }
    }
  }
}
```

## Error Handling

The server handles various error conditions:

- **Connection errors**: When Perplexica instance is not reachable
- **HTTP errors**: Invalid requests or server errors from Perplexica
- **Validation errors**: Invalid parameters or missing required fields
- **JSON parsing errors**: Malformed responses from Perplexica

All errors are returned as tool call results with `isError: true` and descriptive error messages.

## Focus Modes Explained

### webSearch
General web search across the internet. Best for current events, general information, and broad topics.

### academicSearch
Focuses on academic papers, research publications, and scholarly content. Ideal for research questions and scientific topics.

### writingAssistant
Optimized for writing help, content creation, and language assistance. Good for creative writing, editing, and style guidance.

### wolframAlphaSearch
Specialized for mathematical computations, scientific calculations, and data analysis. Uses Wolfram Alpha's computational engine.

### youtubeSearch
Searches YouTube for relevant videos. Useful for tutorials, demonstrations, and video content.

### redditSearch
Searches Reddit discussions and communities. Good for opinions, experiences, and community insights.

## Optimization Modes

### balanced
Provides a good balance between response speed and quality. Recommended for most use cases.

### speed
Prioritizes fast responses over comprehensive analysis. Use when you need quick answers.