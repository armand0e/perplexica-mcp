# Perplexica MCP Server

[![Tests](https://github.com/your-armand0e/perplexica-mcp/workflows/Tests/badge.svg)](https://github.com/armand0e/perplexica-mcp/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Model Context Protocol (MCP) server for interacting with local Perplexica instances. This server provides tools to perform AI-powered searches using your local Perplexica installation.

## Features

- **Search**: Perform AI-powered searches with various focus modes
- **Streaming Support**: Get real-time streaming responses
- **Multiple Focus Modes**: Support for web search, academic search, writing assistant, and more
- **Customizable Models**: Configure chat and embedding models
- **Conversation History**: Maintain context across searches

## Installation

### From Source

```bash
git clone https://github.com/your-username/perplexica-mcp.git
cd perplexica-mcp
pip install -e .
```

### From Git (Direct Install)

```bash
pip install git+https://github.com/your-username/perplexica-mcp.git
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
