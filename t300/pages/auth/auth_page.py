from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.header_login_button = page.locator(
                        "header button.ml-4")

        self.login_title = page.locator("header form")
        self.email_input = page.locator("input[name='email']")
        self.password_input = page.locator("input[type='password']")
        self.login_form = page.locator("form").filter(has=self.email_input)
        self.submit_sign_in_button = self.login_form.locator("button[type='submit']")
        self.profile_link = page.locator("header div > a > div > span")

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
