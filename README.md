# TYPLES DOCS

This project uses `UV` as Python package and project manager, written in Rust: https://docs.astral.sh/uv/

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