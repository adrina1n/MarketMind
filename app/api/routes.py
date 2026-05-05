from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


@router.post("/generate")
async def generate(
    request: Request,
    client: str = Form(...),
    sector: str = Form(...),
    geography: str = Form(...),
):
    return templates.TemplateResponse(
        "partials/results.html",
        {
            "request": request,
            "client": client,
            "sector": sector,
            "geography": geography,
        },
    )
