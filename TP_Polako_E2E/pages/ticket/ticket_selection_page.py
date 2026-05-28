from playwright.sync_api import expect

from TP_Polako_E2E.base.base_page import BasePage

CART_BUTTON = "(//button[@aria-label='Cart'])[1]"
PAY_BUTTON = "//button[contains(@class, 'w-full rounded-xl')]"
CART_SIDEBAR = '//h2[@class="text-lg font-bold"]'
ADD_FIRTS_TICKET_BUTTON = "(//article//button)[2]"
ADD_SECOND_TICKET_BUTTON = "(//article//button)[4]"
ADD_THIRD_TICKET_BUTTON = "(//article//button)[6]"
CART_TIMER = "span.bg-blue-100"


class TicketSelectionPage(BasePage):

    def select_test_ticket(self):
        button = self.page.locator(ADD_SECOND_TICKET_BUTTON)
        button.wait_for(state="visible", timeout=10000)
        button.click()

    def select_testo123_ticket(self):
        button = self.page.locator(ADD_FIRTS_TICKET_BUTTON)
        button.wait_for(state="visible", timeout=10000)
        button.click()

    def select_test321_ticket(self):
        button = self.page.locator(ADD_THIRD_TICKET_BUTTON)
        button.wait_for(state="visible", timeout=10000)
        button.click()

    def open_cart(self):
        self.page.locator(CART_BUTTON).wait_for(state="visible", timeout=5000)
        self.page.locator(CART_BUTTON).click()

    def assert_pay_button_is_visible(self):
        pay_button = self.page.locator(PAY_BUTTON).last
        expect(pay_button).to_be_visible(timeout=10000)

    def assert_ticket_title_in_cart(self, expected_title: str):
        ticket_locator = (
            self.page.locator(CART_SIDEBAR)
            .get_by_text(expected_title, exact=True)
            .first
        )
        expect(ticket_locator).to_be_visible(timeout=10000)

    def assert_cart_timer_is_visible(self):
        timer_locator = self.page.locator(CART_TIMER).first
        expect(timer_locator).to_be_visible(timeout=10000)
