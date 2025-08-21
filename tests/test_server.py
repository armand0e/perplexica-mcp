"""Tests for the Perplexica MCP server."""

import pytest
from unittest.mock import AsyncMock, patch
from perplexica_mcp.server import (
    PerplexicaClient,
    SearchRequest,
    SearchResponse,
    SearchSource,
)


@pytest.mark.asyncio
async def test_perplexica_client_search():
    """Test the PerplexicaClient search functionality."""
    # Mock response data
    mock_response_data = {
        "message": "Test response message",
        "sources": [
            {
                "pageContent": "Test content",
                "metadata": {"title": "Test Title", "url": "https://example.com"},
            }
        ],
    }

    with patch("httpx.AsyncClient") as mock_client_class:
        # Setup mock
        mock_client = AsyncMock()
        mock_client_class.return_value = mock_client

        mock_response = AsyncMock()
        mock_response.json = lambda: mock_response_data  # Make it a regular function
        mock_response.raise_for_status = lambda: None  # Make it a regular function
        mock_client.post = AsyncMock(return_value=mock_response)

        # Test
        client = PerplexicaClient("http://localhost:3000")
        request = SearchRequest(query="test query", focusMode="webSearch")

        result = await client.search(request)

        # Assertions
        assert isinstance(result, SearchResponse)
        assert result.message == "Test response message"
        assert len(result.sources) == 1
        assert result.sources[0].pageContent == "Test content"
        assert result.sources[0].metadata["title"] == "Test Title"

        # Verify the HTTP call
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "http://localhost:3000/api/search"


@pytest.mark.asyncio
async def test_perplexica_client_get_models():
    """Test the PerplexicaClient get_models functionality."""
    mock_models_data = {
        "chatModels": {"openai": {"gpt-4o-mini": {"displayName": "GPT 4 omni mini"}}},
        "embeddingModels": {
            "openai": {
                "text-embedding-3-large": {"displayName": "Text Embedding 3 Large"}
            }
        },
    }

    with patch("httpx.AsyncClient") as mock_client_class:
        # Setup mock
        mock_client = AsyncMock()
        mock_client_class.return_value = mock_client

        mock_response = AsyncMock()
        mock_response.json = lambda: mock_models_data  # Make it a regular function
        mock_response.raise_for_status = lambda: None  # Make it a regular function
        mock_client.get = AsyncMock(return_value=mock_response)

        # Test
        client = PerplexicaClient("http://localhost:3000")
        result = await client.get_models()

        # Assertions
        assert result == mock_models_data
        assert "chatModels" in result
        assert "embeddingModels" in result

        # Verify the HTTP call
        mock_client.get.assert_called_once_with("http://localhost:3000/api/models")


def test_search_request_validation():
    """Test SearchRequest model validation."""
    # Valid request
    request = SearchRequest(query="test query", focusMode="webSearch")
    assert request.query == "test query"
    assert request.focusMode == "webSearch"
    assert request.optimizationMode == "balanced"  # default value
    assert request.stream is False  # default value

    # Test with all fields
    request_full = SearchRequest(
        query="test query",
        focusMode="academicSearch",
        optimizationMode="speed",
        stream=True,
        history=[["human", "Hello"], ["assistant", "Hi there"]],
        systemInstructions="Be helpful",
    )
    assert request_full.optimizationMode == "speed"
    assert request_full.stream is True
    assert len(request_full.history) == 2


def test_search_response_parsing():
    """Test SearchResponse model parsing."""
    data = {
        "message": "Test message",
        "sources": [
            {
                "pageContent": "Content 1",
                "metadata": {"title": "Title 1", "url": "https://example1.com"},
            },
            {
                "pageContent": "Content 2",
                "metadata": {"title": "Title 2", "url": "https://example2.com"},
            },
        ],
    }

    response = SearchResponse(**data)
    assert response.message == "Test message"
    assert len(response.sources) == 2
    assert response.sources[0].pageContent == "Content 1"
    assert response.sources[1].metadata["title"] == "Title 2"
