# TYPLES DOCS
#### System that extracts and save information from documents

This project uses `UV` as Python package and project manager, written in Rust: https://docs.astral.sh/uv/

On macOS install with homebrew:
```bash
brew install uv
```

## Running the project

### Running server in dev mode to reload on changes

```bash
uv run uvicorn src.server:app --reload
```
## Run database
To run the database, you need to have Docker installed on your machine. Once you have Docker installed, you can run the following command from the root directory of the project:

```bash
Run from root:
```bash
docker compose up
```

## API documentation

The API documentation (Swagger UI) is available at:
http://localhost:8000/docs

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

### PDF invoices Dataset source
I got invoices PDFs that I want to process with Typless here on [kaggle](https://www.kaggle.com/datasets/ayoubcherguelaine/company-documents-dataset)

### Typless API

I trained new document type on [Typless app](https://app.typless.com/). Than use this document type named `demo-invoice` to process documents.