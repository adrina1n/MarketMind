from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.schemas import ReportSection

client = TestClient(app)


def _wrap(md: str) -> list[ReportSection]:
    return [
        ReportSection(
            category="market_size",
            title="Taille de marche",
            markdown=md,
            sources=[],
            confidence=0.5,
        )
    ]


def test_markdown_tables_render_to_html():
    md = "| Col A | Col B |\n|-------|-------|\n| 1     | 2     |"

    with patch(
        "app.api.routes.generate_report",
        new_callable=AsyncMock,
        return_value=_wrap(md),
    ):
        resp = client.post(
            "/api/generate",
            data={"client": "C", "sector": "S", "geography": "G"},
        )

    assert "<table>" in resp.text
    assert "<td>1</td>" in resp.text


def test_markdown_headers_and_bold_render():
    md = "## Section\n\nTexte **important** ici."

    with patch(
        "app.api.routes.generate_report",
        new_callable=AsyncMock,
        return_value=_wrap(md),
    ):
        resp = client.post(
            "/api/generate",
            data={"client": "C", "sector": "S", "geography": "G"},
        )

    assert "<h2>" in resp.text
    assert "<strong>important</strong>" in resp.text
