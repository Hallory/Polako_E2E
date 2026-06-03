from pages.events.event_form_page import EventFormPage


class CreateEventPage(EventFormPage):
    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.get_by_text("Create event")
        self.submit_button = page.get_by_role("button", name="Create")

    def navigate_to_create(self):
        from data.constants import BASE_URL

        self.page.goto(f"{BASE_URL}/en/user/create-event")
        self.page.wait_for_timeout(3000)
