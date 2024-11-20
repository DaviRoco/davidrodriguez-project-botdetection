from dataclasses import dataclass
from datetime import date


@dataclass
class UrlRatio:
    user_id: str
    record_date: date
    total_requests: int
    distinct_urls: int
    url_ratio: float
