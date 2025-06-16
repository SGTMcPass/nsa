# Contributing to NASA Simulation Agents

Thank you for your interest in contributing to NASA Simulation Agents! We appreciate your time and effort in helping us improve this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style and Standards](#code-style-and-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [License](#license)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/nasa-simulation-agents.git
   cd nasa-simulation-agents
   ```
3. **Set up the development environment**:
   ```bash
   make setup
   ```
4. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

1. **Make your changes** following the code style guidelines.
2. **Run tests** to ensure everything works:
   ```bash
   make test
   ```
3. **Format and lint** your code:
   ```bash
   make format
   make lint
   ```
4. **Commit your changes** with a descriptive message:
   ```bash
   git commit -m "feat: add new feature"
   ```
5. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** against the `main` branch.

## Code Style and Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use type hints for all function signatures and variables.
- Write docstrings following the [Google style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
- Keep lines under 88 characters (Black's default).
- Use `snake_case` for variables and functions, `PascalCase` for classes.

### Pre-commit Hooks

We use pre-commit hooks to enforce code quality. They will run automatically before each commit. To install:

```bash
pre-commit install
```

## Testing

- Write tests for all new features and bug fixes.
- Run tests locally before submitting a PR:
  ```bash
  make test
  ```
- Aim for good test coverage (90%+).

## Documentation

- Update documentation when adding new features or changing behavior.
- Document all public APIs with docstrings.
- Keep the README and other documentation up to date.

## Pull Request Process

1. Ensure your branch is up to date with the target branch.
2. Run all tests and ensure they pass.
3. Update documentation as needed.
4. Open a PR with a clear title and description.
5. Reference any related issues.
6. Request reviews from maintainers.
7. Address all review comments.

## Reporting Issues

When reporting issues, please include:

- A clear, descriptive title.
- Steps to reproduce the issue.
- Expected vs. actual behavior.
- Environment details (Python version, OS, etc.).
- Any relevant logs or error messages.

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).

---

Thank you for contributing to NASA Simulation Agents! 🚀
