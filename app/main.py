from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.api.routes import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title=settings.app_name)
app.mount("/static", StaticFiles(directory=BASE_DIR.parent / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


app.include_router(router, prefix="/api")
