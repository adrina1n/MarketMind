from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryConfig:
    name: str
    title: str
    search_queries: list[str]
    synthesis_prompt: str
