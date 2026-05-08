import re

from app.core.llm import complete
from app.models.schemas import ReportSection, SourcedResult
from app.pipeline.categories.base import CategoryConfig
from app.pipeline.scoring import compute_confidence
from app.pipeline.synthesis.base import Synthesizer

_MISSING_MARKERS = [
    "non disponible",
    "aucune donnee",
    "pas de donnees",
    "a approfondir",
]

_MISSING_PATTERN = re.compile(
    r"[^.\n]*(?:non disponible|aucune donn[ée]e|pas de donn[ée]es|"
    r"a approfondir|information.{0,20}manquante|donn[ée]e.{0,20}incertain)[^.\n]*",
    re.IGNORECASE,
)


def _detect_data_unavailable(md: str) -> bool:
    lower = md.lower()
    return sum(1 for m in _MISSING_MARKERS if m in lower) >= 2


def _extract_missing_details(md: str) -> list[str]:
    matches = _MISSING_PATTERN.findall(md)
    seen: set[str] = set()
    details: list[str] = []
    for m in matches:
        cleaned = m.strip(" \t-*•>")
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            details.append(cleaned)
    return details


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

        confidence = compute_confidence(results)
        data_available = not _detect_data_unavailable(markdown)
        missing_details = _extract_missing_details(markdown)
        if not data_available:
            confidence = min(confidence, 0.3)

        return ReportSection(
            category=category.name,
            title=category.title,
            markdown=markdown,
            sources=results,
            confidence=confidence,
            data_available=data_available,
            missing_details=missing_details,
        )
