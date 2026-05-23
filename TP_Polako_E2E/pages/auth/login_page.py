import os

import pytest

from TP_Polako_E2E.base.base_page import BasePage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage

LOGIN_MODAL_OPEN_BTN = 'button[class="ml-4 flex justify-between gap-1.5 text-sm"]'
LOGIN_FORM = "//div[contains(@class,'absolute') and contains(@class,'z-[1001]')]"
EMAIL_INPUT = 'input[name="email"]'
PASSWORD_INPUT = 'input[name="password"]'
LOGIN_SUBMIT_BTN = 'button[type="submit"]'
ERROR_MESSAGE = "//div[contains(@class, 'text-red')]"
PROFILE_BTN = 'div[class="ml-4 flex items-center justify-between gap-1.5 text-sm"]'


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
        if self.page.locator(ERROR_MESSAGE).is_visible():
            return self.page.locator(ERROR_MESSAGE).inner_text()
        return ""

    def click_profile(self):
        return self.page.click(PROFILE_BTN)

    def get_credentials(self) -> tuple[str, str]:
        email = os.getenv("VALID_EMAIL")
        password = os.getenv("VALID_PASSWORD")

        if not email or not password:
            pytest.fail("VALID_EMAIL или VALID_PASSWORD not specified in .env")

        return email, password

    def open_login_modal(self):
        self.page.locator(LOGIN_MODAL_OPEN_BTN).click(force=True)
        self.page.locator(LOGIN_FORM).wait_for(
            state="visible",
            timeout=5000,
        )

    def login(
        self,
        email: str,
        password: str,
    ):
        self.page.locator(EMAIL_INPUT).fill(email)
        self.page.locator(PASSWORD_INPUT).fill(password)
        self.page.locator(LOGIN_SUBMIT_BTN).click()

    def login_as_valid_user(self):
        email, password = self.get_credentials()

        self.open_login_modal()
        self.login(
            email,
            password,
        )

        self.wait_for_network_stable()

    def click_profile(self):
        self.page.click(PROFILE_BTN)

    def login_and_go_to_profile(self) -> UserProfilePage:
        self.login_as_valid_user()
        self.click_profile()
        self.wait_for_network_stable()
        return UserProfilePage(self.page)
