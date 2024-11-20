from sqlalchemy.orm import Session
from core.ports.output.ip_usage_repository import IpUsageRepository
from core.domain.ip_usage import IpUsage
from adapters.orm_models.ip_usage_orm import IpUsageORM
from datetime import date


class PostgresIpUsageRepository(IpUsageRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user_ip_address: IpUsage):
        user_ip_address_orm = IpUsageORM(user_id=user_ip_address.user_id, record_date=user_ip_address.record_date,
                                         ip_address=user_ip_address.ip_address)
        self.session.add(user_ip_address_orm)
        self.session.commit()

    def find_by_user_id_and_date(self, user_id: str, record_date: date) -> IpUsage:
        user_ip_address_orm = self.session.query(IpUsageORM).filter_by(user_id=user_id, record_date=record_date).first()
        if user_ip_address_orm:
            return IpUsage(user_id=user_ip_address_orm.user_id, record_date=user_ip_address_orm.record_date,
                           ip_address=user_ip_address_orm.ip_address)
        return None

    def delete_by_user_id_and_date(self, user_id: str, record_date: date):
        user_ip_address_orm = self.session.query(IpUsageORM).filter_by(user_id=user_id, record_date=record_date).first()
        if user_ip_address_orm:
            self.session.delete(user_ip_address_orm)
            self.session.commit()
