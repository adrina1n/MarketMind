import asyncio
import logging

from app.models.schemas import ReportSection, SourcedResult
from app.pipeline.categories import get_all_categories, get_category
from app.pipeline.search.tavily import TavilySearch
from app.pipeline.synthesis.llm_synthesizer import LLMSynthesizer

logger = logging.getLogger(__name__)


async def generate_section(
    client: str,
    sector: str,
    geography: str,
    category_name: str = "market_size",
) -> ReportSection:
    category = get_category(category_name)
    context = {"client": client, "sector": sector, "geography": geography}

    search_engine = TavilySearch()
    synthesizer = LLMSynthesizer()

    queries = [q.format(**context) for q in category.search_queries]
    search_tasks = [search_engine.search(q) for q in queries]
    results_lists = await asyncio.gather(*search_tasks, return_exceptions=True)

    all_results: list[SourcedResult] = []
    seen_urls: set[str] = set()
    for result_list in results_lists:
        if isinstance(result_list, Exception):
            logger.warning("Search query failed: %s", result_list)
            continue
        for r in result_list:
            if r.url not in seen_urls:
                seen_urls.add(r.url)
                all_results.append(r)

    if not all_results:
        return ReportSection(
            category=category.name,
            title=category.title,
            markdown="Aucun resultat de recherche trouve. Verifiez votre cle API Tavily.",
            sources=[],
            confidence=0.0,
            data_available=False,
        )

    return await synthesizer.synthesize(all_results, category, context)


async def generate_report(
    client: str,
    sector: str,
    geography: str,
) -> list[ReportSection]:
    sections: list[ReportSection] = []
    categories = get_all_categories()
    for i, category in enumerate(categories):
        if i > 0:
            await asyncio.sleep(5)
        try:
            section = await generate_section(client, sector, geography, category.name)
            sections.append(section)
        except Exception as e:
            logger.exception("Failed to generate section %s", category.name)
            sections.append(
                ReportSection(
                    category=category.name,
                    title=category.title,
                    markdown=f"Erreur lors de la generation de cette section : {e}",
                    sources=[],
                    confidence=0.0,
                    data_available=False,
                )
            )
    return sections
