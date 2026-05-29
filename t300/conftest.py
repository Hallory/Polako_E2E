import pytest
from data.constants import BASE_URL, MANAGER_USER
from pages.app import App
from utils.api_utils import get_api_auth_state


def create_api_auth_app(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    auth_state = get_api_auth_state(
        BASE_URL, MANAGER_USER["email"], MANAGER_USER["password"]
    )
    page.context.add_cookies(auth_state["cookies"])
    page.goto(BASE_URL)
    return App(page)


@pytest.fixture(scope="function")
def app(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(BASE_URL)
    return App(page)


@pytest.fixture(scope="function")
def manager_app(page):
    return create_api_auth_app(page)


@pytest.fixture(scope="function")
def api_auth_app(page):
    return create_api_auth_app(page)


@pytest.fixture
def auth_profile_app(api_auth_app):
    api_auth_app.profile.open()
    return api_auth_app
