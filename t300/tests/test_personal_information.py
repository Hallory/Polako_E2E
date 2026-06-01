import re
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_personal_information_page_loads(auth_profile_app):
    expect(auth_profile_app.page).to_have_url(re.compile(auth_profile_app.profile.URL))
    expect(auth_profile_app.profile.info_form).to_be_visible()
    expect(auth_profile_app.profile.email_input).to_be_visible()
    expect(auth_profile_app.profile.change_password_form).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_basic_info_form(auth_profile_app):
    expect(auth_profile_app.profile.info_form).to_be_visible()
    expect(auth_profile_app.profile.first_name_input).to_be_visible()
    expect(auth_profile_app.profile.last_name_input).to_be_visible()
    expect(auth_profile_app.profile.save_basic_button).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_change_password_form(auth_profile_app):
    expect(auth_profile_app.profile.new_password_input).to_be_visible()
    expect(auth_profile_app.profile.confirm_password_input).to_be_visible()
    expect(auth_profile_app.profile.confirm_password_button).to_be_visible()


@pytest.mark.smoke
def test_personal_information_has_contact_information(auth_profile_app):
    expect(auth_profile_app.profile.phone_input).to_be_visible()
    expect(auth_profile_app.profile.instagram_input).to_be_visible()
    expect(auth_profile_app.profile.telegram_input).to_be_visible()


@pytest.mark.regression
def test_update_basic_information(auth_profile_app):
    original_first_name = auth_profile_app.profile.first_name_input.input_value()
    original_last_name = auth_profile_app.profile.last_name_input.input_value()

    try:
        auth_profile_app.profile.fill_basic_information("Test", "User")
        auth_profile_app.profile.save_basic_information()

        expect(auth_profile_app.page).to_have_url(re.compile(auth_profile_app.profile.URL))
        expect(auth_profile_app.profile.first_name_input).to_have_value("Test")
        expect(auth_profile_app.profile.last_name_input).to_have_value("User")
    finally:
        auth_profile_app.profile.fill_basic_information(
            original_first_name, original_last_name
        )
        auth_profile_app.profile.save_basic_information()


@pytest.mark.regression
def test_basic_info_inputs_are_editable(auth_profile_app):
    auth_profile_app.profile.fill_basic_information("AutoFirst", "AutoLast")
    expect(auth_profile_app.profile.first_name_input).to_have_value("AutoFirst")
    expect(auth_profile_app.profile.last_name_input).to_have_value("AutoLast")
