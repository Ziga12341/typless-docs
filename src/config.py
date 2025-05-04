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

# AWS S3 credentials
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
# Bucket name
BUCKET_NAME = "document-external-source"
