from app.core.llm import complete
from app.models.schemas import ReportSection, SourcedResult
from app.pipeline.categories.base import CategoryConfig
from app.pipeline.synthesis.base import Synthesizer


class LLMSynthesizer(Synthesizer):
    async def synthesize(
        self,
        results: list[SourcedResult],
        category: CategoryConfig,
        context: dict[str, str],
    ) -> ReportSection:
        formatted = "\n\n".join(
            f"[{i + 1}] {r.title} ({r.domain})\n{r.snippet}"
            for i, r in enumerate(results)
        )

        prompt = category.synthesis_prompt.format(
            **context,
            search_results=formatted,
        )

        markdown = await complete(prompt)

        return ReportSection(
            category=category.name,
            title=category.title,
            markdown=markdown,
            sources=results,
            confidence=min(len(results) / 5, 1.0),
        )
