import os

import pytest

from TP_Polako_E2E.base.base_page import BasePage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage
from TP_Polako_E2E.utils.constants import EXPECTED_ERROR_TEXT

LOGIN_MODAL_OPEN_BTN = 'button[class="ml-4 flex justify-between gap-1.5 text-sm"]'
LOGIN_FORM = "//div[contains(@class,'absolute') and contains(@class,'z-[1001]')]"
EMAIL_INPUT = 'input[name="email"]'
PASSWORD_INPUT = 'input[name="password"]'
LOGIN_SUBMIT_BTN = 'button[type="submit"]'
ERROR_MESSAGE = ".text-center.text-2xl"
PROFILE_BTN = 'div[class="ml-4 flex items-center justify-between gap-1.5 text-sm"]'
FORGOT_PASSWORD_LINK = "form button[type='button']"


class LoginPage(BasePage):

    def open_login_modal(self):
        self.page.locator(LOGIN_MODAL_OPEN_BTN).click(force=True)
        self.page.locator(LOGIN_FORM).wait_for(state="visible", timeout=5000)

    def login(self, email: str, password: str):
        self.page.locator(EMAIL_INPUT).fill(email)
        self.page.locator(PASSWORD_INPUT).fill(password)
        self.page.locator(LOGIN_SUBMIT_BTN).click()

    def is_login_successful(self) -> bool:
        return self.page.locator(PROFILE_BTN).is_hidden()

    def get_error_message(self) -> str:
        error_locator = self.page.locator(ERROR_MESSAGE)
        error_locator.wait_for(state="visible", timeout=5000)
        return error_locator.inner_text()

    def verify_error_message(self, expected_text: str = EXPECTED_ERROR_TEXT):
        actual_text = self.get_error_message()
        assert (
            actual_text == expected_text
        ), f"Verification failed: expected '{expected_text}', but got '{actual_text}'"

    def click_login_button(self):
        self.page.locator(LOGIN_SUBMIT_BTN).click()

    def get_credentials(
        self, email_key: str = "VALID_EMAIL", password_key: str = "VALID_PASSWORD"
    ) -> tuple[str, str]:
        email = os.getenv(email_key)
        password = os.getenv(password_key)

        if not email or not password:
            pytest.fail(f"{email_key} or {password_key} not in file .env")

        return email, password

    def login_as_valid_user(self):
        email, password = self.get_credentials()

        self.open_login_modal()
        self.login(email, password)

    def login_as_simple_user(self):
        email, password = self.get_credentials(
            email_key="SIMPLE_USER_EMAIL", password_key="SIMPLE_USER_PASSWORD"
        )

        self.open_login_modal()
        self.login(email, password)

    def click_profile(self):
        self.page.click(PROFILE_BTN)

    def login_and_go_to_profile(self) -> UserProfilePage:
        self.login_as_valid_user()
        self.click_profile()
        self.wait_for_network_stable()
        return UserProfilePage(self.page)

    def is_login_button_disabled(self) -> bool:
        return self.page.locator(LOGIN_SUBMIT_BTN).is_disabled()

    def fill_login_form(self, email: str, password: str):
        self.page.locator(EMAIL_INPUT).fill(email)
        self.page.locator(PASSWORD_INPUT).fill(password)

    def click_forgot_password(self):
        self.page.locator(FORGOT_PASSWORD_LINK).click()
