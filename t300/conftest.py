import pytest
from data.constants import BASE_URL, MANAGER_USER
from pages.app import App
from utils.api_utils import get_api_auth_state


def create_api_auth_app(page):
    auth_state = get_api_auth_state(
        BASE_URL, MANAGER_USER["email"], MANAGER_USER["password"]
    )

    page.context.add_cookies(auth_state["cookies"])
    page.goto(BASE_URL)

    return App(page)


@pytest.fixture(scope="function")
def app(page):
    page.set_viewport_size({"width": 1366, "height": 768})
    page.goto(BASE_URL)
    return App(page)


@pytest.fixture(scope="function")
def manager_app(page):
    return create_api_auth_app(page)


@pytest.fixture(scope="function")
def api_auth_app(page):
    return create_api_auth_app(page)
