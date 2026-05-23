from TP_Polako_E2E.base.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_success(self):
        self.login_page.login_and_go_to_profile()

        self.user_profile.verify_logout_button_visible()

    def test_access_internal_page_without_ui_login(self, authenticated_page):
        self.user_profile.verify_logout_button_visible()
