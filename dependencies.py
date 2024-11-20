import os

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from adapters.postgres.ip_usage_repository import PostgresIpUsageRepository
from adapters.postgres.url_ratio_repository import PostgresUrlRatioRepository
from core.ports.input.ingest_ip_usage import IngestIpUsage
from core.ports.input.ingest_url_ratio import IngestUrlRatio
from core.ports.output.ip_usage_repository import IpUsageRepository
from core.ports.output.url_ratio_repository import UrlRatioRepository
from core.services.ingest_ip_usage_service import IngestIpUsageService
from core.services.ingest_url_ratio_service import IngestUrlRatioService


def get_session() -> Session:
    engine = create_engine(os.getenv("DATABASE_URL"))
    SES = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SES()
    db = session
    try:
        yield db
    finally:
        db.close()


def get_ip_usage_repository(session: Session = Depends(get_session)) -> IpUsageRepository:
    return PostgresIpUsageRepository(session)


def get_ingest_ip_usage(repository: IpUsageRepository = Depends(get_ip_usage_repository)) -> IngestIpUsage:
    return IngestIpUsageService(repository)


def get_url_ratio_repository(session: Session = Depends(get_session)) -> UrlRatioRepository:
    return PostgresUrlRatioRepository(session)


def get_ingest_url_ratio(repository: UrlRatioRepository = Depends(get_url_ratio_repository)) -> IngestUrlRatio:
    return IngestUrlRatioService(repository)
