import os

from dotenv import load_dotenv

load_dotenv()

# TODO: Move to environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://typless:typless@localhost:5432/extractordb",  # Default for local development
)

# get typless api key from environment variable
TYPLESS_API_KEY = os.environ.get("TYPLESS_API_KEY")
