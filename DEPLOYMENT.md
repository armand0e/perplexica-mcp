# Deployment Instructions

This document provides step-by-step instructions for deploying the Perplexica MCP Server to GitHub.

## Quick Setup

1. **Create a new GitHub repository**:
   - Go to https://github.com/new
   - Repository name: `perplexica-mcp`
   - Description: `MCP server for local Perplexica instances - AI-powered search integration`
   - Make it public
   - Don't initialize with README, .gitignore, or license (we already have them)

2. **Run the setup script**:
   ```bash
   ./setup_repo.sh
   ```

   Follow the prompts and enter your repository URL when asked.

## Manual Setup

If you prefer to set up manually:

1. **Add remote origin**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/perplexica-mcp.git
   ```

2. **Push to GitHub**:
   ```bash
   git branch -M main
   git push -u origin main
   ```

## Post-Deployment Setup

After pushing to GitHub:

1. **Add repository topics**:
   - Go to your repository on GitHub
   - Click the gear icon next to "About"
   - Add topics: `mcp`, `perplexica`, `ai-search`, `claude`, `python`

2. **Enable GitHub Actions**:
   - Actions should be automatically enabled
   - Check the "Actions" tab to see the test workflow

3. **Update README badges**:
   - Replace `armand0e` in the README badges with your actual GitHub username

4. **Set up branch protection** (optional):
   - Go to Settings > Branches
   - Add rule for `main` branch
   - Require status checks to pass before merging

## Publishing to PyPI (Optional)

To publish the package to PyPI:

1. **Create PyPI account** at https://pypi.org/

2. **Install build tools**:
   ```bash
   pip install build twine
   ```

3. **Build the package**:
   ```bash
   python -m build
   ```

4. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

5. **Update installation instructions** in README to use:
   ```bash
   pip install perplexica-mcp
   ```

## Running with uvx

This server can also be run directly using `uvx`, which is part of the `uv` (astral-uv) Python package manager. This method assumes that `uv` is installed and the `perplexica-mcp` package has been published to PyPI by the user/organization `armand0e`.

To run the server using `uvx`, use the following command:

```bash
uvx @armand0e/perplexica-mcp:latest
```

`uvx` will handle the download of the package and its dependencies into a managed environment and then execute the server. This is a convenient way to run the server without a manual installation step.

Ensure that the package `perplexica-mcp` is published on PyPI under the `armand0e` user or organization for this command to work.

## Repository Structure

```
perplexica-mcp/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── test.yml
├── docs/
│   ├── API.md
│   └── SETUP.md
├── examples/
│   ├── basic_usage.py
│   ├── claude_desktop_config.json
│   └── mcp_test.py
├── src/
│   └── perplexica_mcp/
│       ├── __init__.py
│       ├── __main__.py
│       └── server.py
├── tests/
│   ├── __init__.py
│   └── test_server.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── DEPLOYMENT.md
├── LICENSE
├── README.md
├── pyproject.toml
└── setup_repo.sh
```

## Features Included

✅ **Core MCP Server**
- Full MCP protocol implementation
- Two main tools: search and get_models
- Support for all Perplexica focus modes
- Comprehensive error handling

✅ **Testing**
- Complete test suite with pytest
- Async testing support
- Mocked HTTP calls

✅ **Documentation**
- Comprehensive README
- API documentation
- Setup guides
- Contributing guidelines

✅ **GitHub Integration**
- Automated testing workflow
- Issue templates
- Branch protection ready

✅ **Package Management**
- Proper Python packaging
- pip installable
- PyPI ready

## Next Steps

1. Deploy to GitHub using the instructions above
2. Test the GitHub Actions workflow
3. Share with the community
4. Consider publishing to PyPI
5. Add more features based on user feedback

## Support

For questions or issues:
- Open an issue on GitHub
- Check the documentation
- Review existing issues and discussions
