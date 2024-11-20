from core.ports.input.ingest_ip_usage import IngestIpUsage
from core.ports.output.ip_usage_repository import IpUsageRepository
from core.domain.ip_usage import IpUsage
import pandas as pd


class IngestIpUsageService(IngestIpUsage):
    def __init__(self, repository: IpUsageRepository):
        self.repository = repository

    def ingest(self, data: pd.DataFrame):
        required_columns = ["user_id", "date", "ip_address"]
        missing_columns = [column for column in required_columns if column not in data.columns]
        if missing_columns:
            raise ValueError(f"Invalid data format. Missing required columns: {', '.join(missing_columns)}")

        for _, row in data.iterrows():
            ip_usage = IpUsage(
                user_id=row["user_id"],
                record_date=row["date"],
                ip_address=row["ip_address"]
            )
            self.repository.save(ip_usage)
