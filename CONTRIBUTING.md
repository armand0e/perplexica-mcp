# Contributing to Perplexica MCP Server

Thank you for your interest in contributing to the Perplexica MCP Server! This document provides guidelines for contributing to the project.

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/perplexica-mcp.git
   cd perplexica-mcp
   ```

2. **Install in development mode**:
   ```bash
   pip install -e .
   pip install pytest pytest-asyncio black isort mypy
   ```

3. **Set up Perplexica** (for testing):
   - Follow the [Perplexica installation guide](https://github.com/ItzCrazyKns/Perplexica)
   - Ensure it's running on `http://localhost:3000`

## Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

4. **Format code**:
   ```bash
   black src/ tests/
   isort src/ tests/
   ```

5. **Type checking**:
   ```bash
   mypy src/
   ```

6. **Commit and push**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

## Code Style

- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Follow [PEP 8](https://pep8.org/) guidelines
- Use type hints where appropriate
- Write docstrings for public functions and classes

## Testing

- Write tests for all new functionality
- Ensure existing tests continue to pass
- Use pytest for testing
- Mock external dependencies (like HTTP calls to Perplexica)
- Aim for good test coverage

## Documentation

- Update the README.md if adding new features
- Update API documentation in `docs/API.md`
- Add examples for new functionality
- Update the CHANGELOG.md

## Commit Messages

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

## Pull Request Guidelines

1. **Description**: Provide a clear description of what your PR does
2. **Testing**: Ensure all tests pass
3. **Documentation**: Update relevant documentation
4. **Breaking Changes**: Clearly mark any breaking changes
5. **Issue Reference**: Reference any related issues

## Reporting Issues

When reporting issues:
1. Use the provided issue templates
2. Include your environment details
3. Provide steps to reproduce
4. Include error messages and logs
5. Test with the latest version first

## Feature Requests

For feature requests:
1. Check if the feature already exists
2. Describe the use case clearly
3. Explain how it would benefit users
4. Consider implementation complexity

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's goals and vision

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Check existing issues and discussions
- Review the documentation

Thank you for contributing to make Perplexica MCP Server better!