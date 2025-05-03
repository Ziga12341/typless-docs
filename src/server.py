from datetime import date
from typing import Optional

import uvicorn
from fastapi import FastAPI
from sqlmodel import Field, SQLModel


# SQLModel - for saving processed documents to the database
# This is a structure of the table in the database
class ProcessedDocuments(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    # AWS S3 will act like archive file storage
    # uuid from AWS S3 archive - where the document is stored
    s3_uuid: str
    # document url to get a raw document from AWS S3 archive
    document_url: str
    # document name (like "invoice_1.pdf") - TODO: I may add timestamp to name to get a unique name
    document_name: str
    # save uuid document that you get when processing a document with Typless API endpoint
    # example for typless response for object_id: "1cb25cc8-c9fa-4149-9a83-b4ed6a2173b9"
    typless_object_id: str

    # the content of document: extract only document number (like "12345678"), date (like "2023-08-01") and document type (like "invoice")

    # typless api returns "data_type": "STRING" examples: "20190500005890","GB123456789"
    document_number: str
    # typless api returns date in format YYYY-MM-DD - "data_type": "DATE"
    document_date: date
    # typless api returns document type in format "invoice" or "receipt" - "data_type": "STRING"
    document_type: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
