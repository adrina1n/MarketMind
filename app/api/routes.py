import logging
from pathlib import Path

import markdown
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.pipeline.orchestrator import generate_report

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")
logger = logging.getLogger(__name__)

_md = markdown.Markdown(extensions=["tables", "fenced_code"])


@router.post("/generate")
async def generate(
    request: Request,
    client: str = Form(...),
    sector: str = Form(...),
    geography: str = Form(...),
):
    try:
        sections = await generate_report(client, sector, geography)
    except Exception as e:
        logger.exception("Pipeline error")
        return templates.TemplateResponse(
            request,
            "partials/results.html",
            {
                "error": f"Erreur lors de la generation: {e}",
                "sections": [],
            },
        )

    sections_data = []
    for section in sections:
        _md.reset()
        sections_data.append({
            "section": section,
            "html": _md.convert(section.markdown),
        })

    return templates.TemplateResponse(
        request,
        "partials/results.html",
        {
            "sections": sections_data,
            "error": None,
        },
    )
