from data.constants import BASE_URL
from pages.base_page import BasePage


class EventsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.events_page_title = page.get_by_text("My events")
        self.create_event_button = page.get_by_role("button", name="Create event")

    def open(self):
        self.page.goto(f"{BASE_URL}/en/user/manage-events")
        self.page.wait_for_timeout(3000)

    def click_create_event(self):
        self.create_event_button.click()
        self.page.wait_for_timeout(2000)
