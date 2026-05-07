from abc import ABC, abstractmethod

from app.models.schemas import ReportSection, SourcedResult
from app.pipeline.categories.base import CategoryConfig


class Synthesizer(ABC):
    @abstractmethod
    async def synthesize(
        self,
        results: list[SourcedResult],
        category: CategoryConfig,
        context: dict[str, str],
    ) -> ReportSection:
        ...
