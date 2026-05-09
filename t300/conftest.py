import pytest
from data.constants import BASE_URL, MANAGER_USER
from pages.app import App


@pytest.fixture(scope="function")
def app(page):
    page.set_viewport_size({"width": 1366, "height": 768})
    page.goto(BASE_URL)
    return App(page)


@pytest.fixture(scope="function")
def manager_app(app):
    app.auth.login(MANAGER_USER["email"], MANAGER_USER["password"])
    app.auth.should_be_logged_in()

    return app
