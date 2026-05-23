from TP_Polako_E2E.base.base_page import BasePage

SEARCH_INPUT_FIELD = "main input[type='text']"
DELETE_EVENT_BTN = "button[data-tooltip-id^='event-delete-']"
CONFIRM_DELETE_BTN = "div.fixed.inset-0 > div > div > button:nth-child(1)"
RIGHT_PANEL_TITLE = "div[class*='grid-cols-2'] > div:nth-child(2) p:first-of-type"


class EventManagementPage(BasePage):

    def search_event(self, event_name: str):
        self.page.locator(SEARCH_INPUT_FIELD).first.fill(event_name)
        self.wait_for_network_stable()

    def check_title_on_right_panel(self) -> str:
        return self.page.locator(RIGHT_PANEL_TITLE).inner_text()

    def click_delete_event(self):
        self.page.locator(DELETE_EVENT_BTN).click()

    def confirm_deletion(self):
        self.page.locator(CONFIRM_DELETE_BTN).click()

    def refresh_events_page(self):
        self.page.reload()

    def check_title_on_search_panel(self) -> str:
        return self.page.locator(SEARCH_INPUT_FIELD).inner_text()
