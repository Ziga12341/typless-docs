# TYPLES DOCS
#### System that extracts and save information from documents

This project uses `UV` as Python package and project manager, written in Rust: https://docs.astral.sh/uv/

## Running the project

### Running server in dev mode

```bash
rye run fastapi dev src/server.py
```

### Running server in production mode

```bash
rye run fastapi run src/server.py
```

## Formatting

For formating we use `black` and `isort`.

To use black and isort, you need to install them first. You can do this by running the following command:

```bash
uv add black isort
```
Then, you can format your code by running the following command:

```bash
source .venv/bin/activate
black .
isort .
```