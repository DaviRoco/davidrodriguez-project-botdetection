from sqlalchemy import Column, String, Date
from adapters.orm_models.base import Base


class IpUsageORM(Base):
    __tablename__ = 'ip_usage'
    user_id = Column(String, primary_key=True)
    record_date = Column(Date, primary_key=True)
    ip_address = Column(String, nullable=False)