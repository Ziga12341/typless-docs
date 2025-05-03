from datetime import date
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI
from sqlmodel import Field, Session, SQLModel, select

from src.database import sql_engine


# TODO: add example to swagger ui: http://fastapi.tiangolo.com/tutorial/schema-extra-example/#examples-in-json-schema-openapi
# TODO: move this SQLModel to models.py
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


# creates database table
SQLModel.metadata.create_all(sql_engine)


# Dependency: Get the session
def get_session():
    with Session(sql_engine) as session:
        yield session  # Yield allows FastAPI to use it as a dependency


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# create a new entry in the database with a document processed/extracted data
# TODO: add error handling - when request fails
@app.post("/processed-documents/", status_code=201)
async def create_processed_document(
    processed_document: ProcessedDocuments, session: Session = Depends(get_session)
):
    print("Creating processed document entry in the database...")
    # this will add a new entry to the database
    session.add(processed_document)
    session.commit()
    session.refresh(processed_document)
    return processed_document


# TODO: add error handling, filtering is case sensitive (not true search), missing pagination, should add sorting (not required)
# get entries from the database with query parameters that i can search/filter by document number, date and type
@app.get("/processed-documents/")
async def read_processed_documents(
    document_number: Optional[str] = None,
    document_date: Optional[date] = None,
    document_type: Optional[str] = None,
    session: Session = Depends(get_session),
):
    print("Reading processed documents from the database...")
    query = select(ProcessedDocuments)
    if document_number:
        query = query.where(ProcessedDocuments.document_number == document_number)
    if document_date:
        query = query.where(ProcessedDocuments.document_date == document_date)
    if document_type:
        query = query.where(ProcessedDocuments.document_type == document_type)

    # Execute the query at this point
    # this is similar to session.query() which is deprecated
    return session.exec(query).all()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
