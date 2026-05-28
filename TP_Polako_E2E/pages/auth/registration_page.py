from TP_Polako_E2E.utils.constants import (
    COMPANY_REGISTRATION_SUCCESS_MESSAGE,
    COOL_BTN_TEXT,
)

from TP_Polako_E2E.base.base_page import BasePage
from TP_Polako_E2E.pages.auth.login_page import LOGIN_FORM
from TP_Polako_E2E.utils.constants import (
    COMPANY_REGISTRATION_SUCCESS_MESSAGE,
    COOL_BTN_TEXT,
)

NO_ACCOUNT_BTN = "header div.absolute > form + button"
ORGANIZER_TAB_BTN = "div.absolute.right-0 div.border-b button:nth-child(2)"

EMAIL_INPUT = 'input[name="email"]'
PASSWORD_INPUT = 'input[name="password"]'
FIRST_NAME_INPUT = 'input[name="first_name"]'
NEXT_BTN = "header div.absolute form button.btn-accent"

COMPANY_NAME_INPUT = 'input[name="company_name"]'
COMPANY_NAME_ERROR = (
    'header div.absolute form div:has(> input[name="company_name"]) span'
)
REGISTER_BTN = 'header div.absolute form button[type="submit"]'

CAPCHA_TOKEN = "aHEqAAAAAEvjOmDiC4CVVh16pgaXcFHpQAgt"

RECAPTCHA_VERIFY_BTN = "#recaptcha-verify-button"

SUCCESS_MESSAGE = "div.absolute.right-0 p.text-center.text-2xl"
COOL_BTN = "div.absolute.right-0 button.btn-accent"
COMPANY_REGISTRATION_INFORM_MESSAGE = (
    "div.absolute.right-0 div.flex-col p.mt-3.text-base"
)
COMPANY_REGISTRATION_ERROR_MESSAGE = "div.absolute.right-0 > p"


class RegistrationPage(BasePage):

    def go_to_organizer_registration(self):
        self.click(NO_ACCOUNT_BTN)
        self.page.locator(LOGIN_FORM).wait_for(state="visible", timeout=5000)
        self.click(ORGANIZER_TAB_BTN)

    def fill_first_step_form(self, email: str, password: str, first_name: str):
        self.fill(EMAIL_INPUT, email)
        self.fill(PASSWORD_INPUT, password)
        self.fill(FIRST_NAME_INPUT, first_name)
        self.click(NEXT_BTN)

    def fill_company_name(self, company_name: str):
        self.fill(COMPANY_NAME_INPUT, company_name)

    def verify_company_name_error_visible(self, expected_error_text):
        self.verify_element_is_visible(COMPANY_NAME_ERROR, expected_error_text)

    def click_register(self):
        self.click(REGISTER_BTN)

    def verify_success_registration(self):
        self.verify_element_is_visible(
            SUCCESS_MESSAGE, COMPANY_REGISTRATION_ERROR_MESSAGE, timeout=10000
        )
        self.verify_element_is_visible(COOL_BTN, COOL_BTN_TEXT)

    def click_cool_button(self):
        self.click(COOL_BTN)

    def verify_failure_inform_message_company_registration(self):
        self.verify_element_is_visible(
            COMPANY_REGISTRATION_INFORM_MESSAGE, COMPANY_REGISTRATION_ERROR_MESSAGE
        )
