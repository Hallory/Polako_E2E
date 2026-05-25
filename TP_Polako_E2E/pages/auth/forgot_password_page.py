from utils.constants import EXPECTED_EMAIL_FORMAT_ERROR_MESSAGE

from TP_Polako_E2E.base.base_page import BasePage

RECOVERY_EMAIL_INPUT = 'input[name="email"]'
SEND_BTN = "form button[type='submit']"
EMAIL_FORMAT_ERROR_LOCATOR = "div.border-b p"
SUCCESS_MODAL_TEXT = "header  p.text-center.text-base"


class ForgotPasswordPage(BasePage):

    def fill_recovery_email(self, email: str):
        self.fill(RECOVERY_EMAIL_INPUT, email)

    def click_send_button(self):
        self.click(SEND_BTN)

    def verify_recovery_success_message(self, email: str):

        self.verify_element_is_visible(
            SUCCESS_MODAL_TEXT, f"{SUCCESS_MODAL_TEXT} {email}"
        )

    def verify_email_format_error_message(self):

        self.verify_element_is_visible(
            EMAIL_FORMAT_ERROR_LOCATOR, EXPECTED_EMAIL_FORMAT_ERROR_MESSAGE
        )
