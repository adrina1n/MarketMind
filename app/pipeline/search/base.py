from abc import ABC, abstractmethod

from app.models.schemas import SourcedResult


class SearchEngine(ABC):
    @abstractmethod
    async def search(self, query: str, max_results: int = 5) -> list[SourcedResult]:
        ...
