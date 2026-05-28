import pytest

from TP_Polako_E2E.utils.constants import (
    EXPECTED_ERROR_TEXT_COMPANY_NAME,
    LONG_COMPANY_NAME,
    TEST_EMAIL,
    TEST_NAME,
    VALID_COMPANY_NAME,
    VALID_TEST_PASSWORD,
    generate_random_email,
    generate_random_user_name,
    generate_random_company_name,
    generate_random_password,
)

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.pages.auth.registration_page import (
    REGISTER_BTN,
    COMPANY_REGISTRATION_INFORM_MESSAGE,
)


class TestRegistration(BaseTest):

    @pytest.mark.skip(reason="Blocked by CAPTCHA limitation")
    def test_positive_manager_registration(self):
        random_email = generate_random_email()
        random_user_name = generate_random_user_name()
        random_company_name = generate_random_company_name()
        random_password = generate_random_password()

        self.login_page.open_login_modal()
        self.registration_page.go_to_organizer_registration()
        self.registration_page.fill_first_step_form(random_email, random_password, random_user_name)
        self.registration_page.fill_company_name(random_company_name)
        self.registration_page.click_register()
        self.registration_page.verify_success_registration()


    def test_invalid_company_name_registration(self):
        self.login_page.open_login_modal()
        self.registration_page.go_to_organizer_registration()
        self.registration_page.fill_first_step_form(TEST_EMAIL, VALID_TEST_PASSWORD, TEST_NAME)
        self.registration_page.fill_company_name(LONG_COMPANY_NAME)
        self.registration_page.verify_company_name_error_visible(EXPECTED_ERROR_TEXT_COMPANY_NAME)

        assert self.page.locator(REGISTER_BTN).is_disabled()


    @pytest.mark.skip(reason="Blocked by CAPTCHA limitation")
    def test_email_has_already_been_registered(self):
        self.login_page.open_login_modal()
        self.registration_page.go_to_organizer_registration()
        self.registration_page.fill_first_step_form(TEST_EMAIL, VALID_TEST_PASSWORD, TEST_NAME)
        self.registration_page.fill_company_name(VALID_COMPANY_NAME)
        self.registration_page.click_register()
        self.registration_page.verify_failure_inform_message_company_registration()

        assert self.page.locator(COMPANY_REGISTRATION_INFORM_MESSAGE)
