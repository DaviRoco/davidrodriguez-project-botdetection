import csv
import io
import os

from fastapi import FastAPI, UploadFile, File
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import dbSchema
app = FastAPI()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


dbSchema.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename.endswith(".csv"):
        contents = await file.read()
        csv_data = io.StringIO(contents.decode("utf-8"))
        csv_reader = csv.DictReader(csv_data)
        json_data = [row for row in csv_reader]
        return json_data
    else:
        return {"message": "Only .csv files allowed."}
