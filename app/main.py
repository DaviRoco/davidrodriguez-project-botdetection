import csv
import io
import os

from fastapi import FastAPI, UploadFile, File, Depends
from app.ports.csv_ports import CsvPort
from app.adapters.csv_adapters import CsvAdapter
from app.adapters.db_adapter import DatabaseAdapter
from app.db_session import session
app = FastAPI()

csv_port = CsvPort()
db_adapter = DatabaseAdapter(db_session=session)
csv_adapter = CsvAdapter(csv_port=csv_port, db_port=db_adapter)


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        return await csv_adapter.handle_uploaded_file(file)
    except ValueError as e:
        return {"message": str(e)}
