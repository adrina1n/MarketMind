from pydantic import BaseModel


class SourcedResult(BaseModel):
    title: str
    snippet: str
    url: str
    domain: str
    relevance_score: float = 0.0


class ReportSection(BaseModel):
    category: str
    title: str
    markdown: str
    sources: list[SourcedResult]
    confidence: float
    data_available: bool = True
    missing_details: list[str] = []
