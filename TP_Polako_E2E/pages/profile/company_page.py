from TP_Polako_E2E.base.base_page import BasePage

COMPANY_NAME_TITLE = ".text-2xl.font-bold"
UPLOAD_INPUT = 'input[type="file"]'
EMAIL_INPUT = 'input[placeholder="email@company.com"]'
PHONE_INPUT = 'input[placeholder="+381..."]'
DESCRIPTION_FIELD = ".w-e-text-container"
SAVE_CHANGES_BTN = "button:has-text('save')"


class CompanyPage(BasePage):
    def get_company_name(self) -> str:
        return self.get_text(COMPANY_NAME_TITLE)

    def upload_logo(self, file_path: str):
        self.page.set_input_files(UPLOAD_INPUT, file_path)

    def set_contact_info(self, email: str, phone: str):
        self.fill(EMAIL_INPUT, email)
        self.fill(PHONE_INPUT, phone)

    def set_description(self, text: str):
        self.fill(DESCRIPTION_FIELD, text)

    def save_company_settings(self):
        self.click(SAVE_CHANGES_BTN)
        self.wait_for_network_stable()
