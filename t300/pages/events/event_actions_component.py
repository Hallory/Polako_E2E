from pages.base_page import BasePage


class EventActionsComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.delete_buttons = page.get_by_role("button", name="Delete")
        self.event_cards = page.locator("[data-testid='event-card']")

    def delete_event_by_title(self, event_title: str):
        event_card = self.page.locator("div").filter(has_text=event_title)
        delete_button = event_card.locator("button", has_text="Delete").first
        delete_button.click()
        self.page.wait_for_timeout(3000)

    def get_delete_button_for_event(self, event_title: str):
        event_card = self.page.locator("div").filter(has_text=event_title)
        return event_card.locator("button", has_text="Delete").first

    def get_toaster(self):
        return (
            self.page.locator("[role='alert']")
            or self.page.locator(".toast")
            or self.page.locator(".notification")
        )

    def wait_for_success_notification(self, timeout: int = 5000):
        try:
            self.page.get_by_text("deleted").first.wait_for(timeout=timeout)
        except:
            self.page.locator("[role='alert']").first.wait_for(timeout=timeout)
