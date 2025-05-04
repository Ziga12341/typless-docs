import boto3
from dotenv import load_dotenv

from .config import AWS_ACCESS_KEY, AWS_SECRET_KEY

load_dotenv()

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)
