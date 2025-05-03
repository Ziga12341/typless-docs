import os

# TODO: Move to environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://typless:typless@localhost:5432/extractordb",  # Default for local development
)
