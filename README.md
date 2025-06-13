# Perplexica MCP Server

A Model Context Protocol (MCP) server for interacting with local Perplexica instances. This server provides tools to perform AI-powered searches using your local Perplexica installation.

## Features

- **Search**: Perform AI-powered searches with various focus modes
- **Streaming Support**: Get real-time streaming responses
- **Multiple Focus Modes**: Support for web search, academic search, writing assistant, and more
- **Customizable Models**: Configure chat and embedding models
- **Conversation History**: Maintain context across searches

## Installation

```bash
pip install -e .
```

## Configuration

The server connects to a local Perplexica instance. By default, it expects Perplexica to be running on `http://localhost:3000`.

You can configure the base URL by setting the `PERPLEXICA_BASE_URL` environment variable:

```bash
export PERPLEXICA_BASE_URL=http://localhost:3001
```

## Usage

### With Claude Desktop

Add this to your Claude Desktop configuration:

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

### Available Tools

- `perplexica_search`: Perform AI-powered searches with various focus modes
- `perplexica_get_models`: Get available chat and embedding models

## Focus Modes

- `webSearch`: General web search
- `academicSearch`: Academic and research-focused search
- `writingAssistant`: Writing and content creation assistance
- `wolframAlphaSearch`: Mathematical and computational queries
- `youtubeSearch`: YouTube video search
- `redditSearch`: Reddit discussion search

## Requirements

- Python 3.8+
- A running Perplexica instance (see [Perplexica GitHub](https://github.com/ItzCrazyKns/Perplexica))