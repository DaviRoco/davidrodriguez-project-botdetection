from core.ports.input.ingest_url_ratio import IngestUrlRatio
from core.ports.output.url_ratio_repository import UrlRatioRepository
from core.domain.url_ratio import UrlRatio
import pandas as pd


class IngestUrlRatioService(IngestUrlRatio):
    def __init__(self, repository: UrlRatioRepository):
        self.repository = repository

    def ingest(self, data: pd.DataFrame):
        required_columns = ["user_id", "date", "total_requests", "distinct_urls", "url_ratio"]
        missing_columns = [column for column in required_columns if column not in data.columns]
        if missing_columns:
            raise ValueError(f"Invalid data format. Missing required columns: {', '.join(missing_columns)}")

        for _, row in data.iterrows():
            user_url_ratio = UrlRatio(
                user_id=row["user_id"],
                record_date=row["date"],
                total_requests=row["total_requests"],
                distinct_urls=row["distinct_urls"],
                url_ratio=row["url_ratio"]
            )
            self.repository.save(user_url_ratio)
