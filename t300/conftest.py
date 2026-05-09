import pytest
from pages.app import App
from data.constants import BASE_URL


@pytest.fixture(scope="function")
def app(page):
    page.goto(BASE_URL)
    return App(page)
