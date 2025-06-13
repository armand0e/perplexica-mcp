#!/bin/bash

# Script to set up GitHub repository for Perplexica MCP Server
# Run this script after creating a GitHub repository manually

echo "Perplexica MCP Server - Repository Setup"
echo "========================================"
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

# Get repository URL from user
echo "Please create a new repository on GitHub first:"
echo "1. Go to https://github.com/new"
echo "2. Repository name: perplexica-mcp"
echo "3. Description: MCP server for local Perplexica instances - AI-powered search integration"
echo "4. Make it public"
echo "5. Don't initialize with README, .gitignore, or license (we already have them)"
echo ""

read -p "Enter your GitHub repository URL (e.g., https://github.com/username/perplexica-mcp.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "Error: Repository URL is required"
    exit 1
fi

# Add remote origin
echo "Adding remote origin..."
git remote add origin "$REPO_URL"

# Create main branch and push
echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "Your Perplexica MCP Server is now available at:"
echo "$REPO_URL"
echo ""
echo "Next steps:"
echo "1. Add topics/tags to your repository: mcp, perplexica, ai-search, claude"
echo "2. Consider adding a GitHub Actions workflow for testing"
echo "3. Add the repository to package registries if desired"
echo ""
echo "To install the package:"
echo "pip install git+$REPO_URL"