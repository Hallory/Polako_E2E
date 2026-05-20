from TP_Polako_E2E.base.base_page import BasePage


class ReportsPage(BasePage):
    DOWNLOAD_REPORT_BTN = 'button[data-type="download-pdf"]'
    DATE_FILTER = 'input[name="report-date"]'

    def download_last_report(self):
        with self.page.expect_download() as download_info:
            self.click(self.DOWNLOAD_REPORT_BTN)
        return download_info.value

    def filter_by_date(self, date_str: str):
        self.fill(self.DATE_FILTER, date_str)
