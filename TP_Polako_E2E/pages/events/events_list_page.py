from TP_Polako_E2E.base.base_page import BasePage

EVENT_CARD = '[data-testid="event-card"]'
EVENT_TITLE = ".event-card__title"
FILTER_BUTTON = "button.filters-trigger"
SEARCH_INPUT = 'input[placeholder*="search"]'
CREATE_EVENT_BTN = "a[href$='/user/events/create"


class EventsListPage(BasePage):
    def search_event(self, query: str):
        self.fill(SEARCH_INPUT, query)
        self.page.keyboard.press("Enter")

    def open_event_by_index(self, index: int = 0):
        self.page.locator(EVENT_CARD).nth(index).click()

    def get_all_event_titles(self):
        return self.page.locator(EVENT_TITLE).all_inner_texts()

    def create_event_btn_is_visible(self):
        self.page.locator(CREATE_EVENT_BTN).is_visible()

    def click_create_event_btn(self):
        self.page.locator(CREATE_EVENT_BTN).click()
