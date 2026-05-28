import pytest

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.utils.constants import (EMAIL_ADDRESS, INVALID_EMAILS)


class TestForgotPassword(BaseTest):

    @pytest.mark.xfail(reason="Bug on Staging: Returns Error Instead of Success")
    def test_forgot_password_success(self):
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()
        self.forgot_password_page.fill_recovery_email(EMAIL_ADDRESS)
        self.forgot_password_page.click_send_button()
        self.forgot_password_page.verify_recovery_success_message(EMAIL_ADDRESS)

    @pytest.mark.xfail(reason="Bug on Staging: Returns Success Instead of Error")
    def test_forgot_password_invalid_email(self):
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()
        invalid_email = INVALID_EMAILS[0]
        self.forgot_password_page.fill_recovery_email(invalid_email)
        self.forgot_password_page.click_send_button()
        self.forgot_password_page.verify_email_format_error_message()


    def test_forgot_password_with_empty_email(self):
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()
        self.forgot_password_page.verify_send_button_is_disabled()


    def test_navigation_to_forgot_password_page(self):
        self.login_page.open_login_modal()
        self.login_page.click_forgot_password()
        self.forgot_password_page.verify_recovery_page_is_displayed()


