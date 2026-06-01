from pages.base_page import BasePage


class AccountSidebar(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.sidebar = page.locator("nav").filter(
            has=page.locator("a[href*='personal-information']")
        )

        self.profile_link = self.sidebar.locator("a[href*='personal-information']")
        self.purchases_link = self.sidebar.locator("a[href*='purchases']")
        self.company_link = self.sidebar.locator("a[href*='company-settings']")
        self.manage_events_link = self.sidebar.locator("a[href*='events']")
        self.contract_data_link = self.sidebar.locator("a[href*='contract-data']")
        self.contracts_link = self.sidebar.locator("a[href*='contracts']")
        self.reports_link = self.sidebar.locator("a[href*='reports']")
        self.create_qr_link = self.sidebar.locator("a[href*='qr-generator']")
        self.withdrawal_link = self.sidebar.locator("a[href*='withdrawal']")
        self.management_link = self.sidebar.locator("a[href*='management']")
        self.publication_link = self.sidebar.locator("a[href*='publications']")
        self.balance_link = self.sidebar.locator("a[href*='balance']")

    def open_profile(self):
        self.close_whats_new_modal()
        self.profile_link.click()

    def open_purchases(self):
        self.close_whats_new_modal()
        self.purchases_link.click()

    def open_company(self):
        self.close_whats_new_modal()
        self.company_link.click()

    def open_manage_events(self):
        self.close_whats_new_modal()
        self.manage_events_link.click()

    def open_contract_data(self):
        self.close_whats_new_modal()
        self.contract_data_link.click()

    def open_contracts(self):
        self.close_whats_new_modal()
        self.contracts_link.click()

    def open_reports(self):
        self.close_whats_new_modal()
        self.reports_link.click()

    def open_create_qr(self):
        self.close_whats_new_modal()
        self.create_qr_link.click()

    def open_withdrawal(self):
        self.close_whats_new_modal()
        self.withdrawal_link.click()

    def open_management(self):
        self.close_whats_new_modal()
        self.management_link.click()

    def open_publication(self):
        self.close_whats_new_modal()
        self.publication_link.click()

    def open_balance(self):
        self.close_whats_new_modal()
        self.balance_link.click()
