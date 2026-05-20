from TP_Polako_E2E.base.base_page import BasePage

CREATE_EVENT_BTN = "flex-col gap-2"
EVENT_ROW = '[data-testid="event-item"]'
STATUS_LABEL = ".status-indicator"
EDIT_ICON = "svg.edit-icon"
ACTION_MENU = 'button[aria-haspopup="menu"]'


class EventManagementPage(BasePage):
    def start_creating_event(self):
        self.click(CREATE_EVENT_BTN)

    def get_event_status_by_index(self, index: int = 0) -> str:
        return self.page.locator(STATUS_LABEL).nth(index).inner_text()

    def open_actions_for_event(self, index: int = 0):
        self.page.locator(ACTION_MENU).nth(index).click()
