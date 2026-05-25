from pages.base_page import BasePage


class AccountSidebar(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.sidebar = (
            page.locator("nav").filter(has_text="Personal").filter(has_text="Organizer")
        )

        self.profile_link = self.sidebar.locator(
            "a[href='/en/user/personal-information']"
        )
        self.purchases_link = self.sidebar.locator("a[href='/en/user/purchases']")
        self.company_link = self.sidebar.locator("a[href='/en/user/company-settings']")
        self.manage_events_link = self.sidebar.locator("a[href='/en/user/events']")
        self.contract_data_link = self.sidebar.locator("a[href='/en/user/contract-data']")
        self.contracts_link = self.sidebar.locator("a[href='/en/user/contracts']")
        self.reports_link = self.sidebar.locator("a[href='/en/user/reports']")
        self.create_qr_link = self.sidebar.locator("a[href='/en/user/qr-generator']")
        self.withdrawal_link = self.sidebar.locator("a[href='/en/user/withdrawal']")

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
