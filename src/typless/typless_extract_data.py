"""
I create a new document type in the Typless dashboard (https://app.typless.com/) for the invoice named              invoice_10248.pdf. I created a new document type named demo-invoice.
I will use this document type to test the document processing and extraction in this project.

for async use data extraction: https://docs.typless.com/reference/post-extract-data-async
and https://docs.typless.com/reference/get-get-extraction-data
when using async endpoint use tupless notification webhook for optimal asynchronous usage: https://docs.typless.com/docs/webhooks
"""

import base64

import requests
from dotenv import load_dotenv

from src.config import TYPLESS_API_KEY


# TODO: add error handling - when request fails, add docs for function.
# TODO: add async call to the API (also you need to change the endpoint to /extract-data-async and /get-extraction-data)
# typless api key is stored in the .env file and accessed through the config.py file
# note: it always takes supplier_name... VINET but for this system it doesn't matter
def process_document(file_name, document_type_name):
    """
    Process a document through the Typless API for data extraction.
    """
    # Load environment variables
    load_dotenv()

    # Read and encode the file
    with open(file_name, "rb") as file:
        base64_data = base64.b64encode(file.read()).decode("utf-8")

    url = "https://developers.typless.com/api/extract-data"

    payload = {
        "file": base64_data,
        "file_name": file_name,
        "document_type_name": document_type_name,
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": TYPLESS_API_KEY,
    }

    # Make the API request
    response = requests.request("POST", url, json=payload, headers=headers)

    # Return the JSON response
    return response.json()


if __name__ == "__main__":
    from typless_parser import parse_response

    file_name = "invoice_10248.pdf"  # invoice_number: 10248
    file_name_2 = "invoice_10249.pdf"  # invoice_number: 10249
    document_type_name = "demo-invoice"
    process_pdf_1 = process_document(
        file_name=file_name, document_type_name=document_type_name
    )
    print(parse_response(process_pdf_1))
    print(f"object_id: {process_pdf_1["object_id"]}")
    for field in process_pdf_1["extracted_fields"]:
        print(f'{field["name"]}: {field["values"][0]["value"]}')
