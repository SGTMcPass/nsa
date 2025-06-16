# NASA Simulation Agents - Development Guide

This document provides guidelines and instructions for developing and maintaining the NASA Simulation Agents project.

## Table of Contents

- [Development Environment Setup](#development-environment-setup)
- [Code Style and Formatting](#code-style-and-formatting)
- [Testing](#testing)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Type Checking](#type-checking)
- [Documentation](#documentation)
- [Version Control](#version-control)
- [CI/CD](#cicd)
- [Troubleshooting](#troubleshooting)

## Development Environment Setup

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) (recommended) or pip
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/nasa-simulation-agents.git
   cd nasa-simulation-agents
   ```

2. Set up the development environment:
   ```bash
   # Using Make (recommended)
   make setup

   # Or manually
   python -m pip install --upgrade pip
   pip install -e ".[dev]"
   pre-commit install
   ```

## Code Style and Formatting

We use the following tools to maintain code quality:

- **Black** - Code formatting
- **isort** - Import sorting
- **Ruff** - Python linter
- **Flake8** - Additional style checking
- **mypy** - Static type checking

### Auto-formatting

```bash
# Format all Python files
make format

# Or manually
black .
isort .
```

### Linting

```bash
# Run all linters
make lint

# Fix auto-fixable issues
make lint-fix
```

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage report
make test-cov

# Run a specific test file
pytest tests/path/to/test_file.py -v

# Run a specific test function
pytest tests/path/to/test_file.py::test_function_name -v
```

### Writing Tests

- Tests should be placed in the `tests/` directory, mirroring the source structure.
- Use `pytest` for testing framework.
- Name test files with `test_` prefix.
- Use descriptive test function names starting with `test_`.
- Use fixtures for common test setup/teardown.

## Pre-commit Hooks

Pre-commit hooks are configured to automatically run checks before each commit:

- Auto-formatting with Black and isort
- Linting with Ruff and Flake8
- Type checking with mypy
- YAML/JSON validation
- And more...

### Running Manually

```bash
make pre-commit
```

## Type Checking

We use mypy for static type checking:

```bash
make type
```

## Documentation

### Docstrings

Follow Google-style docstrings:

```python
def function_name(param1: type, param2: type) -> return_type:
    """Short description of the function.

    Longer description with more details about the function's behavior,
    parameters, return values, and any exceptions that might be raised.

    Args:
        param1: Description of param1.
        param2: Description of param2.


    Returns:
        Description of the return value.

    Raises:
        ValueError: If something goes wrong.
    """
    pass
```

### Building Documentation

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Build documentation
cd docs
make html

# View documentation
open _build/html/index.html
```

## Version Control

### Branching Strategy

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `release/*` - Release preparation branches

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semi-colons, etc.
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

## CI/CD

### GitHub Actions

- Linting and type checking on every push
- Unit tests on multiple Python versions
- Documentation build on main branch
- Release automation

### Version Bumping

We use `bump2version` to manage version numbers:

```bash
# Install bump2version
pip install bump2version

# Bump patch version (0.1.0 → 0.1.1)
bump2version patch

# Bump minor version (0.1.0 → 0.2.0)
bump2version minor

# Bump major version (0.1.0 → 1.0.0)
bump2version major
```

## Troubleshooting

### Common Issues

#### Pre-commit Hooks Not Running

```bash
# Ensure hooks are installed
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

#### Dependency Issues

```bash
# Clean up existing environment
make clean-all

# Recreate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Reinstall dependencies
make setup
```

#### Test Failures

```bash
# Run with debug output
pytest -vvs tests/

# Run with pdb on failure
pytest --pdb tests/
```

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
