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
        self.info_form = page.locator("form").filter(has=self.basic_information)
        self.change_password = page.get_by_text("Change password", exact=True)
        self.change_password_form = page.locator("form").filter(has=self.change_password)
        
        self.first_name_input = self.info_form.get_by_placeholder("First name")
        self.last_name_input = self.info_form.get_by_placeholder("Last name")
        self.save_button = self.info_form.get_by_role("button", name="Save")
    def should_be_on_profile_page(self):
        expect(self.page).to_have_url(re.compile(self.URL))
        expect(self.profile).to_be_visible()
        expect(self.basic_information).to_be_visible()
        expect(self.contact_information).to_be_visible()
        
    def have_basic_information_form(self):
        expect(self.info_form).to_be_visible()
        
    def have_change_password_form(self):
        expect(self.change_password_form).to_be_visible()
        
    def have_contact_information(self):
        expect(self.contact_information).to_be_visible()
        
    def fill_basic_information(self, first_name, last_name):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        
    def save_changes(self):
        self.save_button.click()