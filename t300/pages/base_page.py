class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title

    def close_whats_new_modal(self):
        modal = self.page.locator("[role='dialog'][aria-labelledby='whats-new-title']")

        if not modal.is_visible():
            return

        try:
            modal.locator("button").last.click()
        except Exception:
            self.page.keyboard.press("Escape")
