from dataclasses import dataclass
from datetime import date


@dataclass
class IpUsage:
    user_id: str
    record_date: date
    ip_address: str
