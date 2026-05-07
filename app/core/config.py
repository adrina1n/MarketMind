from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MarketMind"
    debug: bool = True
    gemini_api_key: str = ""
    tavily_api_key: str = ""

    model_config = {"env_file": ".env"}


settings = Settings()
