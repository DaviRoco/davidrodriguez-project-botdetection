from abc import ABC, abstractmethod
import pandas as pd


class IngestServiceInterface(ABC):
    @abstractmethod
    def ingest(self, data: pd.DataFrame):
        pass
