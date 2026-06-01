import pytest
from data.constants import BASE_URL, MANAGER_USER
from pages.app import App
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from utils.api_utils import get_api_auth_state


def create_api_auth_app(page, auth_state):
    page.context.clear_cookies()
    page.context.add_cookies(auth_state["cookies"])
    return App(page)


@pytest.fixture(scope="function")
def app(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(BASE_URL)
    return App(page)


@pytest.fixture(scope="session")
def api_auth_state():
    return get_api_auth_state(
        BASE_URL, MANAGER_USER["email"], MANAGER_USER["password"]
    )


@pytest.fixture(scope="function")
def manager_app(page, api_auth_state):
    return create_api_auth_app(page, api_auth_state)


@pytest.fixture(scope="function")
def api_auth_app(page, api_auth_state):
    return create_api_auth_app(page, api_auth_state)


@pytest.fixture(scope="session")
def auth_profile_app(browser, api_auth_state):
    context = browser.new_context()
    context.add_cookies(api_auth_state["cookies"])
    page = context.new_page()
    app = App(page)

    try:
        with page.expect_response(
            lambda response: "/api/auth/refresh" in response.url and response.ok,
            timeout=10000,
        ):
            page.goto(BASE_URL, wait_until="domcontentloaded")
    except PlaywrightTimeoutError:
        page.goto(BASE_URL, wait_until="domcontentloaded")

    app.profile.open()
    app.profile.close_whats_new_modal()
    yield app
    context.close()
