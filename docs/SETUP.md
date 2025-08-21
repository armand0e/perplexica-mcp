# Perplexica MCP Server Setup Guide

## Prerequisites

1. **Python 3.8+** installed on your system
2. **Perplexica** running locally (see [Perplexica Installation Guide](https://github.com/ItzCrazyKns/Perplexica))
3. **Claude Desktop** (for MCP integration)

## Step 1: Install Perplexica

First, you need to have Perplexica running locally. Follow the official installation guide:

1. Clone the Perplexica repository:
   ```bash
   git clone https://github.com/ItzCrazyKns/Perplexica.git
   cd Perplexica
   ```

2. Follow the setup instructions in the Perplexica README to:
   - Install dependencies
   - Configure your API keys (OpenAI, etc.)
   - Start the Perplexica server

3. Verify Perplexica is running by visiting `http://localhost:3000` in your browser

## Step 2: Install the Perplexica MCP Server

1. Clone this repository:
   ```bash
   git clone https://github.com/armand0e/perplexica-mcp.git
   cd perplexica-mcp
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

   Or install from PyPI (when available):
   ```bash
   pip install perplexica-mcp
   ```

## Step 3: Test the Installation

Test the server directly:

```bash
python -m perplexica_mcp
```

You can also test the client functionality:

```bash
python examples/basic_usage.py
```

## Step 4: Configure Claude Desktop

1. Locate your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add the Perplexica MCP server configuration:

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

3. If you have other MCP servers, add the perplexica configuration to the existing `mcpServers` object.

## Step 5: Restart Claude Desktop

1. Completely quit Claude Desktop
2. Restart Claude Desktop
3. You should see the Perplexica tools available in Claude

## Configuration Options

### Environment Variables

- **PERPLEXICA_BASE_URL**: URL of your Perplexica instance (default: `http://localhost:3000`)

### Custom Perplexica Port

If your Perplexica instance runs on a different port, update the configuration:

```json
{
  "mcpServers": {
    "perplexica": {
      "command": "python",
      "args": ["-m", "perplexica_mcp"],
      "env": {
        "PERPLEXICA_BASE_URL": "http://localhost:3001"
      }
    }
  }
}
```

### Multiple Perplexica Instances

You can configure multiple Perplexica instances:

```json
{
  "mcpServers": {
    "perplexica-main": {
      "command": "python",
      "args": ["-m", "perplexica_mcp"],
      "env": {
        "PERPLEXICA_BASE_URL": "http://localhost:3000"
      }
    },
    "perplexica-dev": {
      "command": "python",
      "args": ["-m", "perplexica_mcp"],
      "env": {
        "PERPLEXICA_BASE_URL": "http://localhost:3001"
      }
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **"Connection refused" errors**
   - Ensure Perplexica is running on the specified port
   - Check the `PERPLEXICA_BASE_URL` configuration
   - Verify firewall settings

2. **"Module not found" errors**
   - Ensure the package is installed: `pip install -e .`
   - Check Python path and virtual environment

3. **Claude Desktop doesn't show Perplexica tools**
   - Verify the configuration file syntax (valid JSON)
   - Check Claude Desktop logs for errors
   - Restart Claude Desktop completely

4. **Permission errors**
   - Ensure Python has necessary permissions
   - Check file permissions on the configuration

### Debugging

Enable debug logging by setting environment variables:

```json
{
  "mcpServers": {
    "perplexica": {
      "command": "python",
      "args": ["-m", "perplexica_mcp"],
      "env": {
        "PERPLEXICA_BASE_URL": "http://localhost:3000",
        "DEBUG": "1"
      }
    }
  }
}
```

### Testing Connection

Test the connection to Perplexica manually:

```bash
curl -X GET http://localhost:3000/api/models
```

This should return a JSON response with available models.

## Usage Examples

Once configured, you can use Perplexica in Claude Desktop:

1. **Basic search**: "Use Perplexica to search for information about quantum computing"

2. **Academic search**: "Search for recent academic papers on machine learning using Perplexica's academic search"

3. **YouTube search**: "Find YouTube videos about Python programming using Perplexica"

4. **Get available models**: "Show me what models are available in Perplexica"

## Next Steps

- Explore the [API Documentation](API.md) for detailed tool usage
- Check out the [examples](../examples/) directory for more usage patterns
- Contribute to the project on GitHub
