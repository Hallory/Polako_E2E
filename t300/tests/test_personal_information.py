import re

import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_personal_information_happy_path_api_auth(api_auth_app):
    """
    Happy path test: API auth + open profile + verify main elements visible
    Uses larger timeouts (2-3s) as app is slow
    """
    # Navigate to profile page
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)

    # Assert we're on the correct page
    expect(api_auth_app.page).to_have_url(re.compile(api_auth_app.profile.URL))

    # Assert main sections are visible
    expect(api_auth_app.profile.basic_information_heading).to_be_visible()
    expect(api_auth_app.profile.email_input).to_be_visible()
    expect(api_auth_app.profile.change_password_heading).to_be_visible()

    # Assert sidebar is visible with profile link
    expect(api_auth_app.sidebar.profile_link).to_be_visible()


@pytest.mark.smoke
def test_personal_information_page_loads(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.page).to_have_url(re.compile(api_auth_app.profile.URL))
    expect(api_auth_app.sidebar.profile_link).to_be_visible()
    expect(api_auth_app.profile.basic_information_heading).to_be_visible()
    expect(api_auth_app.profile.email_input).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_basic_info_form(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.profile.info_form).to_be_visible()
    expect(api_auth_app.profile.first_name_input).to_be_visible()
    expect(api_auth_app.profile.last_name_input).to_be_visible()
    expect(api_auth_app.profile.save_basic_button).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_change_password_form(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.profile.new_password_input).to_be_visible()
    expect(api_auth_app.profile.confirm_password_input).to_be_visible()
    expect(api_auth_app.profile.confirm_password_button).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_contact_information(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.profile.email_input).to_be_visible()
    expect(api_auth_app.profile.phone_input).to_be_visible()
    expect(api_auth_app.profile.instagram_input).to_be_visible()
    expect(api_auth_app.profile.telegram_input).to_be_visible()


@pytest.mark.smoke
def test_sidebar_visible_on_profile_page(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.sidebar.sidebar).to_be_visible()
    expect(api_auth_app.sidebar.profile_link).to_be_visible()


@pytest.mark.regression
def test_update_basic_information(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    original_first_name = api_auth_app.profile.first_name_input.input_value()
    original_last_name = api_auth_app.profile.last_name_input.input_value()

    try:
        api_auth_app.profile.fill_basic_information("Test", "User")
        api_auth_app.profile.save_basic_information()
        api_auth_app.page.wait_for_timeout(2000)

        expect(api_auth_app.page).to_have_url(re.compile(api_auth_app.profile.URL))
        expect(api_auth_app.profile.first_name_input).to_have_value("Test")
        expect(api_auth_app.profile.last_name_input).to_have_value("User")
    finally:
        api_auth_app.profile.fill_basic_information(
            original_first_name, original_last_name
        )
        api_auth_app.profile.save_basic_information()


@pytest.mark.regression
def test_basic_info_inputs_are_editable(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.page.wait_for_timeout(2000)
    api_auth_app.profile.fill_basic_information("AutoFirst", "AutoLast")
    api_auth_app.page.wait_for_timeout(1000)
    expect(api_auth_app.profile.first_name_input).to_have_value("AutoFirst")
    expect(api_auth_app.profile.last_name_input).to_have_value("AutoLast")


@pytest.mark.regression
def test_sidebar_navigate_to_profile(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.sidebar.open_profile()
    api_auth_app.page.wait_for_timeout(2000)
    expect(api_auth_app.page).to_have_url(re.compile(api_auth_app.profile.URL))


@pytest.mark.regression
def test_sidebar_navigate_to_purchases(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.sidebar.open_purchases()
    api_auth_app.profile.page.wait_for_url("**/user/**")


@pytest.mark.regression
def test_sidebar_navigate_to_company(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.sidebar.open_company()
    api_auth_app.profile.page.wait_for_url("**/user/**")


@pytest.mark.regression
def test_sidebar_navigate_to_manage_events(api_auth_app):
    api_auth_app.profile.open()
    api_auth_app.sidebar.open_manage_events()
    api_auth_app.profile.page.wait_for_url("**/user/**")
