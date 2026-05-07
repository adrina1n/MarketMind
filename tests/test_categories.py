import pytest

from app.pipeline.categories import CATEGORIES, get_all_categories, get_category
from app.pipeline.categories.base import CategoryConfig

EXPECTED_CATEGORIES = [
    "market_size",
    "market_environment",
    "competitors",
    "client_profile",
    "client_strategy",
]


def test_all_five_categories_registered():
    assert len(CATEGORIES) == 5
    for name in EXPECTED_CATEGORIES:
        assert name in CATEGORIES


def test_get_category_returns_config():
    for name in EXPECTED_CATEGORIES:
        cat = get_category(name)
        assert isinstance(cat, CategoryConfig)
        assert cat.name == name
        assert len(cat.search_queries) > 0
        assert len(cat.synthesis_prompt) > 0


def test_get_all_categories_returns_list():
    cats = get_all_categories()
    assert len(cats) == 5
    names = [c.name for c in cats]
    for name in EXPECTED_CATEGORIES:
        assert name in names


def test_get_unknown_category_raises():
    with pytest.raises(KeyError):
        get_category("does_not_exist")


def test_all_categories_have_template_placeholders():
    for cat in get_all_categories():
        for query in cat.search_queries:
            assert "{sector}" in query or "{client}" in query
        assert "{search_results}" in cat.synthesis_prompt
        assert "{client}" in cat.synthesis_prompt
