from playwright.sync_api import Page, Response, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> Response | None:
        return self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def verify_element_is_visible(self, selector: str, element_name: str = "Element"):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def hover(self, locator: str):
        self.page.locator(locator).hover()

    def scroll_into_view(self, locator: str):
        self.page.locator(locator).scroll_into_view_if_needed()

    def expect_url(self, url_part: str):
        expect(self.page).to_have_url(lambda url: url_part in url)

    def wait_for_network_stable(self):
        self.page.wait_for_load_state("networkidle")
