import asyncio
import logging

from google import genai

from app.core.config import settings

logger = logging.getLogger(__name__)

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


async def complete(prompt: str, model: str = "gemini-2.5-flash", max_retries: int = 3) -> str:
    client = _get_client()
    for attempt in range(max_retries):
        try:
            response = await client.aio.models.generate_content(
                model=model,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            if attempt < max_retries - 1 and ("503" in str(e) or "UNAVAILABLE" in str(e) or "429" in str(e)):
                wait = 2 ** attempt * 3
                logger.warning("Gemini %s, retry in %ds (attempt %d/%d)", e, wait, attempt + 1, max_retries)
                await asyncio.sleep(wait)
            else:
                raise
