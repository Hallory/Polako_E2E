from TP_Polako_E2E.base.base_page import BasePage
from TP_Polako_E2E.utils.constants import EXPECTED_EMAIL_FORMAT_ERROR_MESSAGE

RECOVERY_EMAIL_INPUT = 'input[name="email"]'
SEND_BTN = "form button[type='submit']"
EMAIL_FORMAT_ERROR_LOCATOR = "div.absolute.right-0 div.flex-col p.mt-3.text-base"
SUCCESS_MODAL_TEXT = "header  p.text-center.text-base"
RECOVERY_TITLE = "div.absolute.right-0 > p.whitespace-nowrap.text-2xl"


class ForgotPasswordPage(BasePage):

    def fill_recovery_email(self, email: str):
        self.fill(RECOVERY_EMAIL_INPUT, email)

    def click_send_button(self):
        self.click(SEND_BTN)

    def verify_recovery_success_message(self, email: str):
        self.verify_element_is_visible(SUCCESS_MODAL_TEXT, f"{SUCCESS_MODAL_TEXT} {email}")

    def verify_email_format_error_message(self):
        self.verify_element_is_visible(EMAIL_FORMAT_ERROR_LOCATOR, EXPECTED_EMAIL_FORMAT_ERROR_MESSAGE)

    def verify_recovery_page_is_displayed(self):
        self.verify_element_is_visible(RECOVERY_TITLE)

    def verify_send_button_is_disabled(self):
        self.page.locator(SEND_BTN).is_disabled()