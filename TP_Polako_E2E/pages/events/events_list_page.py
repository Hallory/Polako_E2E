from TP_Polako_E2E.base.base_page import BasePage

EVENT_CARD = '[data-testid="event-card"]'
EVENT_TITLE = ".event-card__title"
FILTER_BUTTON = "button.filters-trigger"
SEARCH_INPUT = 'input[placeholder*="search"]'
CREATE_EVENT_BTN = "div.mb-4  span "
TITLE_FIELD = "form>section:nth-child(2)>div:nth-child(2)  input"
DESCRIPTION_FIELD = "div[class*='w-md-editor-input'] textarea"
CALENDAR_WIDGET_FIELD = 'input[icon="bg-phiCalendar"]'
DATE_TODAY_SELECTION = "button.rdp-day_today, button[aria-current='date']"
DURATION_FIELD = "form>section:nth-child(2)>div:nth-child(3)>div>div>input"
CATEGORY_FIELD = "form>section:nth-child(2)>div:nth-child(4)>div:nth-child(1)>div>span"
CATEGORY_OPTION = (
    "form>section:nth-child(2)>div:nth-child(4)>div:nth-child(1)>ul>div:nth-child(2)"
)
LANGUAGE_FIELD = (
    "form>section:nth-child(2)>div:nth-child(4)>div:nth-child(2)>div>div>span"
)
LANGUAGE_CATEGORY = "form>section:nth-child(2)>div:nth-child(4)>div:nth-child(2) div:nth-child(1)>button"
PRICE_FIELD = "form>section:nth-child(2)>div:nth-child(5) span.bg-phiCaretDown"
PRICE_TYPE = "form>section:nth-child(2)>div:nth-child(5) ul>div.bg-accent>button"
VISIT_COST_FIELD = "form>section:nth-child(2)>div:nth-child(5)>div:nth-child(2) input"
LOCATION_FIELD = "form>section:nth-child(2)>div:nth-child(6)>div>div>div>input"
UPLOAD_INPUT = 'input[type="file"]'
SAVE_BUTTON = "form>div>div>button"
CREATE_EVENT_BTN = "btn-accent w-60 text-center"


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

    def fill_title_field(self, title: str):
        self.page.locator(TITLE_FIELD).click()
        self.fill(TITLE_FIELD, title)

    def fill_description_field(self, description: str):
        self.page.locator(DESCRIPTION_FIELD).click()
        self.fill(DESCRIPTION_FIELD, description)

    def select_current_date(self):
        self.page.locator(CALENDAR_WIDGET_FIELD).click()
        self.page.locator(DATE_TODAY_SELECTION).click()

    def fill_duration_field(self, duration: str):
        self.page.locator(DURATION_FIELD).click()
        self.fill(DURATION_FIELD, duration)

    def select_category_field(self):
        self.page.locator(CATEGORY_FIELD).click()

    def select_category_option(self):
        self.page.locator(CATEGORY_OPTION).click()

    def select_language_field(self):
        self.page.locator(LANGUAGE_FIELD).click()

    def select_language_option(self):
        self.page.locator(LANGUAGE_CATEGORY).click()

    def select_price_field(self):
        self.page.locator(PRICE_FIELD).click()

    def select_price_type(self):
        self.page.locator(PRICE_TYPE).click()

    def fill_visit_cost_field(self, visit_cost: str):
        self.page.locator(VISIT_COST_FIELD).click()
        self.fill(VISIT_COST_FIELD, visit_cost)

    def fill_location_field(self, location: str):
        self.page.locator(LOCATION_FIELD).click()
        self.fill(LOCATION_FIELD, location)

    def upload_image_field(self, file_path: str):
        self.page.set_input_files(UPLOAD_INPUT, file_path)

    def click_save_event_btn(self):
        self.page.locator(SAVE_BUTTON).click()
