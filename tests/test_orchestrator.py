from unittest.mock import AsyncMock, patch

import pytest

from app.models.schemas import ReportSection, SourcedResult
from app.pipeline.orchestrator import generate_report, generate_section


def _make_result(url: str, title: str = "T") -> SourcedResult:
    return SourcedResult(title=title, snippet="s", url=url, domain="d.com")


@pytest.mark.asyncio
async def test_deduplicates_results_by_url():
    duplicate = _make_result("https://a.com/1", "dup")
    unique = _make_result("https://b.com/2", "unique")

    async def fake_search(self, query, max_results=5):
        return [duplicate, unique, duplicate]

    with (
        patch("app.pipeline.orchestrator.TavilySearch.search", new=fake_search),
        patch(
            "app.pipeline.orchestrator.LLMSynthesizer.synthesize",
            new_callable=AsyncMock,
            return_value=ReportSection(
                category="market_size",
                title="T",
                markdown="ok",
                sources=[],
                confidence=1.0,
            ),
        ) as mock_synth,
    ):
        await generate_section("C", "S", "G")
        call_args = mock_synth.call_args
        results_passed = call_args[0][0]
        urls = [r.url for r in results_passed]
        assert len(urls) == len(set(urls))
        assert len(urls) == 2


@pytest.mark.asyncio
async def test_all_searches_fail_returns_error_section():
    async def failing_search(self, query, max_results=5):
        raise RuntimeError("API down")

    with patch("app.pipeline.orchestrator.TavilySearch.search", new=failing_search):
        section = await generate_section("C", "S", "G")

    assert isinstance(section, ReportSection)
    assert section.confidence == 0.0
    assert section.sources == []
    assert "Aucun" in section.markdown


@pytest.mark.asyncio
async def test_generate_report_returns_all_sections():
    async def fake_search(self, query, max_results=5):
        return [_make_result("https://example.com/" + query[:10])]

    with (
        patch("app.pipeline.orchestrator.TavilySearch.search", new=fake_search),
        patch(
            "app.pipeline.orchestrator.LLMSynthesizer.synthesize",
            new_callable=AsyncMock,
            return_value=ReportSection(
                category="test",
                title="T",
                markdown="content",
                sources=[],
                confidence=1.0,
            ),
        ),
    ):
        sections = await generate_report("C", "S", "G")

    assert len(sections) == 5
    assert all(isinstance(s, ReportSection) for s in sections)
