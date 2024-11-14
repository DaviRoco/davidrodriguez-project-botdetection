from typing import List, Dict

from fastapi import UploadFile
from app.ports.db_port import DatabasePort


class CsvAdapter:
    def __init__(self, csv_port, db_port: DatabasePort):
        self.csv_port = csv_port
        self.db_port = db_port

    async def handle_uploaded_file(self, file: UploadFile) -> bool:
        if file.filename.endswith(".csv"):
            contents = await file.read()
            data = self.csv_port.process_csv(contents.decode("utf-8"))
            self.db_port.save(data)
            return True
        else:
            raise ValueError("Only .csv files allowed.")
