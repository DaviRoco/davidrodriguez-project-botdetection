from sqlalchemy import Column, String, Integer, Float, Date
from adapters.orm_models.base import Base


class UrlRatioORM(Base):
    __tablename__ = 'url_ratio'
    user_id = Column(String, primary_key=True)
    record_date = Column(Date, primary_key=True)
    total_requests = Column(Integer, nullable=False)
    distinct_urls = Column(Integer, nullable=False)
    url_ratio = Column(Float, nullable=False)
