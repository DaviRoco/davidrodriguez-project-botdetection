from abc import abstractmethod
import pandas as pd
from core.ports.input.ingest_service_interface import IngestServiceInterface


class IngestUrlRatio(IngestServiceInterface):
    
    @abstractmethod
    def ingest(self, data: pd.DataFrame):
        pass