from utils.constants import (EXPECTED_ERROR_TEXT_COMPANY_NAME,
                             LONG_COMPANY_NAME, TEST_EMAIL, TEST_NAME,
                             VALID_COMPANY_NAME, VALID_TEST_PASSWORD)

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.pages.auth.registration_page import \
    REGISTER_BTN  # <-- Добавляем импорт REGISTER_BTN


class TestRegistration(BaseTest):

    def test_positive_manager_registration(self):

        self.login_page.open_login_modal()

        self.registration_page.go_to_organizer_registration()

        self.registration_page.fill_first_step_form(
            TEST_EMAIL, VALID_TEST_PASSWORD, TEST_NAME
        )

        self.registration_page.fill_company_name(VALID_COMPANY_NAME)

        self.registration_page.click_register()

        self.registration_page.verify_success_registration()
        self.registration_page.click_cool_button()

    def test_invalid_company_name_registration(self):

        self.login_page.open_login_modal()
        self.registration_page.go_to_organizer_registration()

        self.registration_page.fill_first_step_form(
            TEST_EMAIL, VALID_TEST_PASSWORD, TEST_NAME
        )

        self.registration_page.fill_company_name(LONG_COMPANY_NAME)

        self.registration_page.verify_company_name_error_visible(
            EXPECTED_ERROR_TEXT_COMPANY_NAME
        )

        assert self.page.locator(
            REGISTER_BTN
        ).is_disabled(), (
            "The registration button must be disabled in case of a validation error!"
        )
