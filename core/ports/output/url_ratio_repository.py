from abc import ABC, abstractmethod
from datetime import date
from core.domain.url_ratio import UrlRatio


class UrlRatioRepository(ABC):
    @abstractmethod
    def save(self, url_ratio: UrlRatio):
        pass

    @abstractmethod
    def find_by_user_id_and_date(self, user_id: str, record_date: date) -> UrlRatio:
        pass

    @abstractmethod
    def delete_by_user_id_and_date(self, user_id: str, record_date: date):
        pass
