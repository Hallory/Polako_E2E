import pytest
from data.constants import BASE_URL, MANAGER_USER
from pages.app import App
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from utils.api_utils import get_api_auth_state


def create_api_auth_app(page):
    profile_url = f"{BASE_URL.rstrip('/')}/user/personal-information"

    for attempt in range(2):
        auth_state = get_api_auth_state(
            BASE_URL, MANAGER_USER["email"], MANAGER_USER["password"]
        )

        page.context.clear_cookies()
        page.context.add_cookies(auth_state["cookies"])

        try:
            with page.expect_response(
                lambda response: "/api/auth/refresh" in response.url and response.ok
            ):
                page.goto(BASE_URL, wait_until="domcontentloaded")

            page.goto(profile_url, wait_until="domcontentloaded")
            page.wait_for_url("**/user/personal-information**")
            page.locator("input[name='first_name']").wait_for(state="visible")
            break
        except PlaywrightTimeoutError:
            if attempt == 1:
                raise

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
