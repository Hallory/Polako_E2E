from pages.base_page import BasePage
from playwright.sync_api import expect


class AccountSidebar(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.sidebar = (
            page.locator("nav").filter(has_text="Personal").filter(has_text="Organizer")
        )

        self.profile_link = self.sidebar.get_by_role("link", name="Profile")
        self.purchases_link = self.sidebar.get_by_role("link", name="My purchases")
        self.company_link = self.sidebar.get_by_role("link", name="Company")
        self.manage_events_link = self.sidebar.get_by_role("link", name="Manage events")
        self.contract_data_link = self.sidebar.get_by_role("link", name="Contract data")
        self.contracts_link = self.sidebar.get_by_role("link", name="Contracts")
        self.reports_link = self.sidebar.get_by_role("link", name="Reports")
        self.create_qr_link = self.sidebar.get_by_role("link", name="Create QR")
        self.withdrawal_link = self.sidebar.get_by_role("link", name="Withdrawal")

    def open_profile(self):
        self.profile_link.click()

    def open_purchases(self):
        self.purchases_link.click()

    def open_company(self):
        self.company_link.click()

    def open_manage_events(self):
        self.manage_events_link.click()
        
    def open_contract_data(self):
        self.contract_data_link.click()

    def open_contracts(self):
        self.contracts_link.click()

    def open_reports(self):
        self.reports_link.click()

    def open_create_qr(self):
        self.create_qr_link.click()

    def open_withdrawal(self):
        self.withdrawal_link.click()

    def should_have_main_links(self):
        expect(self.sidebar).to_be_visible()
        expect(self.profile_link).to_be_visible()
        expect(self.purchases_link).to_be_visible()
        expect(self.company_link).to_be_visible()
        expect(self.manage_events_link).to_be_visible()
        expect(self.contracts_link).to_be_visible()
        expect(self.reports_link).to_be_visible()
        expect(self.create_qr_link).to_be_visible()
        expect(self.withdrawal_link).to_be_visible()
