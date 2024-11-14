from sqlalchemy import Column, BigInteger, TIMESTAMP, ForeignKey, Double

from .db_session import Base


class UrlRatio(Base):
    __tablename__ = 'url_ratio'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date = Column(TIMESTAMP, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    total_requests = Column(BigInteger, nullable=False)
    distinct_urls = Column(BigInteger, nullable=False)
    url_ratio = Column(Double, nullable=False)
