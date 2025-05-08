# Twitch analytics technical test

Test application used to retrieve twitch analytics.

# Development

## Installation

To install the application you will need the python environment manager **poetry**

### poetry

[Documentation](https://python-poetry.org/docs/)

### Install dependencies

```shell
poetry install
```

### Pre-commit linting

Pre-commit hooks are used to lint all the new code.
The hooks used are defined on the _.pre-commit-config.yaml_ file.

Install pre-commit by running:

```shell
poetry run pre-commit install
```

Run pre-commit:

```shell
poetry run pre-commit run --all-files
```

### Type checking

The mypy tool is used as a python type checker on this project so we can get
type hints and troubleshooting assist.

Run the type checking:

```shell
poetry run mypy --package src
```
