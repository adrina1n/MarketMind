from pydantic import BaseModel


class SourcedResult(BaseModel):
    title: str
    snippet: str
    url: str
    domain: str


class ReportSection(BaseModel):
    category: str
    title: str
    markdown: str
    sources: list[SourcedResult]
    confidence: float
