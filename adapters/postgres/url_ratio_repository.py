from sqlalchemy.orm import Session
from datetime import date
from core.domain.url_ratio import UrlRatio
from core.ports.output.url_ratio_repository import UrlRatioRepository
from adapters.orm_models.url_ratio_orm import UrlRatioORM


class PostgresUrlRatioRepository(UrlRatioRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user_url_ratio: UrlRatio):
        user_url_ratio_orm = UrlRatioORM(user_id=user_url_ratio.user_id, record_date=user_url_ratio.record_date,
                                         total_requests=user_url_ratio.total_requests,
                                         distinct_urls=user_url_ratio.distinct_urls,
                                         url_ratio=user_url_ratio.url_ratio)
        self.session.add(user_url_ratio_orm)
        self.session.commit()

    def find_by_user_id_and_date(self, user_id: str, record_date: date) -> UrlRatio:
        user_url_ratio_orm = self.session.query(UrlRatioORM).filter_by(user_id=user_id, record_date=record_date).first()
        if user_url_ratio_orm:
            return UrlRatio(user_id=user_url_ratio_orm.user_id, record_date=user_url_ratio_orm.record_date,
                            total_requests=user_url_ratio_orm.total_requests,
                            distinct_urls=user_url_ratio_orm.distinct_urls,
                            url_ratio=user_url_ratio_orm.url_ratio)
        return None

    def delete_by_user_id_and_date(self, user_id: str, record_date: date):
        user_url_ratio_orm = self.session.query(UrlRatioORM).filter_by(user_id=user_id, record_date=record_date).first()
        if user_url_ratio_orm:
            self.session.delete(user_url_ratio_orm)
            self.session.commit()
