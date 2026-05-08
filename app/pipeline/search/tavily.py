from urllib.parse import urlparse

import httpx

from app.core.config import settings
from app.models.schemas import SourcedResult
from app.pipeline.search.base import SearchEngine


class TavilySearch(SearchEngine):
    async def search(self, query: str, max_results: int = 5) -> list[SourcedResult]:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": settings.tavily_api_key,
                    "query": query,
                    "max_results": max_results,
                    "search_depth": "basic",
                },
                timeout=30.0,
            )
            resp.raise_for_status()
            data = resp.json()

        return [
            SourcedResult(
                title=r.get("title", ""),
                snippet=r.get("content", ""),
                url=r.get("url", ""),
                domain=urlparse(r.get("url", "")).netloc,
                relevance_score=r.get("score", 0.0),
            )
            for r in data.get("results", [])
        ]
