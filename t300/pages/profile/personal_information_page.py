from data.constants import BASE_URL
from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class PersonalInformationPage(BasePage):
    URL = "/user/personal-information"

    def __init__(self, page):
        super().__init__(page)

        self.profile_nav_link = page.locator("a[href='/en/user/personal-information']")
        self.basic_information_heading = page.get_by_text(
            "Basic information", exact=True
        )
        self.contact_information_heading = page.get_by_text(
            "Contact information", exact=True
        )
        self.change_password_heading = page.locator("p").filter(
            has_text="Change the password"
        ).first

        self.first_name_input = page.locator("input[name='first_name']")
        self.last_name_input = page.locator("input[name='last_name']")
        self.email_input = page.locator("input[name='email']")
        self.phone_input = page.locator("input[name='phone']")
        self.instagram_input = page.locator("input[name='instagram']")
        self.telegram_input = page.locator("input[name='telegram']")

        self.info_form = page.locator("form").filter(has=self.first_name_input)
        self.save_basic_button = self.info_form.locator("button[type='submit']")

        self.new_password_input = page.locator("input[name='new_password']")
        self.confirm_password_input = page.locator("input[name='confirm_password']")
        self.change_password_form = page.locator("form").filter(
            has=self.new_password_input
        )
        self.confirm_password_button = self.change_password_form.locator(
            "button[type='submit']"
        )

    def open(self):
        self.page.goto(f"{BASE_URL.rstrip('/')}{self.URL}", wait_until="domcontentloaded")
        self.page.wait_for_url(f"**{self.URL}**", timeout=10000)
        try:
            self.first_name_input.wait_for(state="visible", timeout=15000)
        except PlaywrightTimeoutError:
            self.page.reload(wait_until="domcontentloaded")
            self.page.wait_for_url(f"**{self.URL}**", timeout=10000)
            self.first_name_input.wait_for(state="visible", timeout=15000)

    def fill_basic_information(self, first_name: str, last_name: str):
        self.first_name_input.clear()
        self.first_name_input.fill(first_name)
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)

    def save_basic_information(self):
        self.save_basic_button.click()

    def save_changes(self):
        self.save_basic_button.click()

    def fill_password(self, new_password: str, confirm_password: str):
        self.new_password_input.fill(new_password)
        self.confirm_password_input.fill(confirm_password)

    def submit_password_change(self):
        self.confirm_password_button.click()
