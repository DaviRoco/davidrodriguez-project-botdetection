from abc import ABC, abstractmethod
from core.domain.ip_usage import IpUsage
from datetime import date


class IpUsageRepository(ABC):
    @abstractmethod
    def save(self, ip_usage: IpUsage):
        pass

    @abstractmethod
    def find_by_user_id_and_date(self, user_id: str, record_date: date) -> IpUsage:
        pass

    @abstractmethod
    def delete_by_user_id_and_date(self, user_id: str, record_date: date):
        pass
