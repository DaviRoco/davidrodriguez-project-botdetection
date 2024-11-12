from abc import ABC, abstractmethod
from typing import List, Dict


class DatabasePort(ABC):
    @abstractmethod
    def save(self, data: List[Dict[str, str]]) -> None:
        pass
