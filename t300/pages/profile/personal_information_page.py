import re

from pages.base_page import BasePage
from playwright.sync_api import expect


class PersonalInformationPage(BasePage):
    URL = "/user/personal-information"

    def __init__(self, page):
        super().__init__(page)

        self.profile = page.locator("nav").get_by_role("link", name="Profile")
        self.basic_information = page.get_by_text("Basic information")
        self.contact_information = page.get_by_text("Contact information", exact=True)
    def should_be_on_profile_page(self):
        expect(self.page).to_have_url(re.compile(self.URL))
        expect(self.profile).to_be_visible()
        expect(self.basic_information).to_be_visible()
        expect(self.contact_information).to_be_visible()
