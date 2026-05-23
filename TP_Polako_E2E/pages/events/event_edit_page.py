from TP_Polako_E2E.base.base_page import BasePage

SAVE_AND_CHECK_BUTTON = "form>div>div button:nth-of-type(2)"
PAGE_TITLE = "form h3:first-of-type"


class EventEditPage(BasePage):

    def get_page_title(self) -> str:
        return self.page.locator(PAGE_TITLE).inner_text()

    def click_save_event_btn(self):
        self.page.locator(SAVE_AND_CHECK_BUTTON).click()
