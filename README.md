# actions-tests

A simple Python project to demonstrate how GitHub Actions works.

## Project Structure

- `calculator.py` - Simple calculator module with sum functions
- `test_calculator.py` - Unit tests using pytest
- `requirements.txt` - Python dependencies
- `.github/workflows/test.yml` - GitHub Actions workflow configuration
- `.devcontainer/devcontainer.json` - VS Code devcontainer configuration

## Features

### Calculator Functions

The calculator module provides two simple functions:

1. **`add(a, b)`** - Adds two numbers together
2. **`add_multiple(*args)`** - Adds multiple numbers together

### Test Suite

The test suite includes 10 test cases covering:
- Positive numbers
- Negative numbers  
- Mixed positive/negative numbers
- Zero values
- Floating point numbers
- Multiple arguments
- Edge cases

## Usage

### Using DevContainer (Recommended)

This project includes a devcontainer configuration for VS Code that provides a consistent development environment:

1. Install [Docker](https://www.docker.com/products/docker-desktop) and [VS Code](https://code.visualstudio.com/)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code
3. Open the project in VS Code
4. Click "Reopen in Container" when prompted (or use Command Palette: "Dev Containers: Reopen in Container")
5. The container will automatically install dependencies and set up the environment

The devcontainer includes:
- Python 3.12
- Git
- Python extension for VS Code
- Pylance language server
- Black formatter
- Ruff linter
- Automatic pytest configuration

### Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the tests:
```bash
pytest -v test_calculator.py
```

3. Use the calculator module:
```python
from calculator import add, add_multiple

result1 = add(2, 3)  # Returns 5
result2 = add_multiple(1, 2, 3, 4, 5)  # Returns 15
```

## GitHub Actions Workflow

The project includes a GitHub Actions workflow that:
- Triggers on pushes and pull requests to main/master branches
- Tests the code on multiple Python versions (3.9, 3.10, 3.11, 3.12)
- Installs dependencies automatically
- Runs the test suite

The workflow file is located at `.github/workflows/test.yml`.

## License

This is a test project for learning GitHub Actions.
