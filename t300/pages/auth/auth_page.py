from pages.base_page import BasePage
from playwright.sync_api import expect


class AuthPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.header_login_button = page.locator("header").get_by_text(
            "Sign In", exact=True
        )
        self.login_title = page.get_by_text("Login to profile")
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.login_form = page.locator("form").filter(has=self.email_input)
        self.submit_sign_in_button = self.login_form.get_by_role(
            "button", name="Sign In"
        )
        self.profile_link = page.locator("header").get_by_role("link", name="Profile")

    def open_login_form(self):
        self.header_login_button.click()

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def login(self, email: str, password: str):
        self.open_login_form()
        self.fill_login_form(email, password)
        self.submit_sign_in_button.click()

    def should_show_login_form(self):
        expect(self.login_title).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.submit_sign_in_button).to_be_visible()

    def should_have_disabled_submit_button(self):
        expect(self.submit_sign_in_button).to_be_disabled()

    def should_have_enabled_submit_button(self):
        expect(self.submit_sign_in_button).to_be_enabled()

    def should_be_logged_in(self):
        expect(self.profile_link).to_be_visible()
