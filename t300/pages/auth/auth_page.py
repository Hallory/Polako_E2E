from pages.base_page import BasePage


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

    def open_profile(self):
        self.profile_link.click()
        self.page.wait_for_url("**/user/personal-information**")
