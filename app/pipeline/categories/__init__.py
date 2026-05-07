from app.pipeline.categories.base import CategoryConfig
from app.pipeline.categories.client_profile import CLIENT_PROFILE
from app.pipeline.categories.client_strategy import CLIENT_STRATEGY
from app.pipeline.categories.competitors import COMPETITORS
from app.pipeline.categories.market_environment import MARKET_ENVIRONMENT
from app.pipeline.categories.market_size import MARKET_SIZE

CATEGORIES: dict[str, CategoryConfig] = {
    MARKET_SIZE.name: MARKET_SIZE,
    MARKET_ENVIRONMENT.name: MARKET_ENVIRONMENT,
    COMPETITORS.name: COMPETITORS,
    CLIENT_PROFILE.name: CLIENT_PROFILE,
    CLIENT_STRATEGY.name: CLIENT_STRATEGY,
}


def get_category(name: str) -> CategoryConfig:
    return CATEGORIES[name]


def get_all_categories() -> list[CategoryConfig]:
    return list(CATEGORIES.values())
