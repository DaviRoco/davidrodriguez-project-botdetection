from typing import List, Dict

from app.ports.db_port import DatabasePort
from sqlalchemy.orm import Session
from app import dbSchema


class DatabaseAdapter(DatabasePort):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, data: List[Dict[str, str]]) -> None:
        for row in data:
            cert = dbSchema.UrlRatio(**row)
            self.db_session.add(cert)
        self.db_session.commit()
