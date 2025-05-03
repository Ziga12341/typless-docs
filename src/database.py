from sqlmodel import create_engine

from src.config import DATABASE_URL

sql_engine = create_engine(DATABASE_URL)
