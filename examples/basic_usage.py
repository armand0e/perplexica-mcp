"""Basic usage example for Perplexica MCP server."""

import asyncio
import json
from perplexica_mcp.server import PerplexicaClient, SearchRequest


async def main():
    """Example of using the Perplexica client directly."""
    client = PerplexicaClient("http://localhost:3000")
    
    try:
        # Get available models
        print("Getting available models...")
        models = await client.get_models()
        print(json.dumps(models, indent=2))
        
        # Perform a basic search
        print("\nPerforming a web search...")
        search_request = SearchRequest(
            query="What is artificial intelligence?",
            focusMode="webSearch",
            optimizationMode="balanced"
        )
        
        result = await client.search(search_request)
        print(f"Answer: {result.message}")
        print(f"Sources: {len(result.sources)} found")
        
        for i, source in enumerate(result.sources[:3], 1):
            print(f"{i}. {source.metadata.get('title', 'Unknown')}")
            print(f"   URL: {source.metadata.get('url', 'Unknown')}")
            print(f"   Content: {source.pageContent[:100]}...")
            print()
        
        # Academic search example
        print("\nPerforming an academic search...")
        academic_request = SearchRequest(
            query="machine learning algorithms comparison",
            focusMode="academicSearch",
            optimizationMode="balanced"
        )
        
        academic_result = await client.search(academic_request)
        print(f"Academic Answer: {academic_result.message[:200]}...")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())