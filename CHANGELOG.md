# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-06-13

### Added
- Initial release of Perplexica MCP Server
- `perplexica_search` tool for AI-powered searches with multiple focus modes
- `perplexica_get_models` tool to retrieve available models
- Support for all Perplexica focus modes:
  - webSearch: General web search
  - academicSearch: Academic and research-focused search
  - writingAssistant: Writing and content creation assistance
  - wolframAlphaSearch: Mathematical and computational queries
  - youtubeSearch: YouTube video search
  - redditSearch: Reddit discussion search
- Configurable optimization modes (speed, balanced)
- Support for custom chat and embedding models
- Conversation history support
- Custom system instructions
- Comprehensive error handling
- Full test suite with pytest
- Documentation and setup guides
- Example usage scripts
- Claude Desktop configuration examples

### Features
- Async HTTP client with proper timeout handling
- Pydantic models for request/response validation
- Environment variable configuration
- Detailed API documentation
- MIT license