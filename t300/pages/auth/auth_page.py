from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")