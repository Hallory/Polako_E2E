import re

from playwright.sync_api import expect


def test_manager_can_open_profile_page(manager_app):
    manager_app.profile.open()

    expect(manager_app.page).to_have_url(re.compile(r".*personal-information.*"))
