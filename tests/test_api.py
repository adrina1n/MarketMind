from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.schemas import ReportSection, SourcedResult

client = TestClient(app)


def _sections() -> list[ReportSection]:
    return [
        ReportSection(
            category="market_size",
            title="Taille de marche",
            markdown="## Taille\nDonnees ici.",
            sources=[
                SourcedResult(
                    title="Source 1",
                    snippet="snip",
                    url="https://example.com/1",
                    domain="example.com",
                )
            ],
            confidence=0.8,
        ),
        ReportSection(
            category="competitors",
            title="Paysage concurrentiel",
            markdown="## Concurrents\nActeurs principaux.",
            sources=[],
            confidence=0.6,
        ),
    ]


def test_generate_returns_html_with_multiple_sections():
    with patch(
        "app.api.routes.generate_report",
        new_callable=AsyncMock,
        return_value=_sections(),
    ):
        resp = client.post(
            "/api/generate",
            data={"client": "LOreal", "sector": "Cosmetique", "geography": "Europe"},
        )

    assert resp.status_code == 200
    html = resp.text
    assert "Taille de marche" in html
    assert "Paysage concurrentiel" in html
    assert "example.com" in html


def test_generate_shows_error_on_pipeline_failure():
    with patch(
        "app.api.routes.generate_report",
        new_callable=AsyncMock,
        side_effect=RuntimeError("boom"),
    ):
        resp = client.post(
            "/api/generate",
            data={"client": "C", "sector": "S", "geography": "G"},
        )

    assert resp.status_code == 200
    assert "Erreur" in resp.text
    assert "boom" in resp.text
