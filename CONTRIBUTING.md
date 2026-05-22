# Contributing to Agentmail Python Library

Thank you for your interest in contributing!

## Development Setup

1. **Install dependencies**

   This project uses [Poetry](https://python-poetry.org/) for dependency management:

   ```sh
   poetry install
   ```

2. **Install pre-commit hooks** (optional but recommended)

   ```sh
   poetry run pre-commit install
   ```

## Testing

Run the test suite with [pytest](https://pytest.org/):

```sh
# Run all tests
poetry run pytest

# Run tests in parallel
poetry run pytest -n auto

# Run with verbose output
poetry run pytest -v
```

## Linting and Type Checking

```sh
# Lint with ruff
poetry run ruff check .

# Type check with mypy
poetry run mypy src/
```

## Pull Request Process

1. **Fork the repository** and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure all tests pass and linting/type checks pass.
4. Update documentation if you've changed any functionality.
5. Submit a pull request targeting the `main` branch.

## Code Style

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting. Please ensure your code adheres to the style guidelines before submitting a PR.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.