import pytest
from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.pages.ticket.ticket_selection_page import TicketSelectionPage
from TP_Polako_E2E.pages.ticket.checkout_page import CheckoutPage
from TP_Polako_E2E.pages.ticket.payment_gateway_page import PaymentGatewayPage
from TP_Polako_E2E.utils.config import Config


class TestTicketPurchase(BaseTest):

    @pytest.mark.ui
    @pytest.mark.smoke
    def test_successful_ticket_checkout_flow(self):

        Config.validate()

        self.login_page.login_as_valid_user()
        ticket_selection = TicketSelectionPage(self.page)
        checkout = CheckoutPage(self.page)
        gateway = PaymentGatewayPage(self.page)


        self.page.goto(
            Config.STG_URL + "/sr/events/ezhegodnyj-rok-koncert-uchenikov-muzykalnoj-shkoly-kreativni-m-kutak-ezhegodnyj-rok-koncer-test-location-ns-2026-05-27-12-00-1")

        ticket_selection.select_free_seat()
        ticket_selection.open_cart()
        ticket_selection.click_buy_button()

        checkout.fill_checkout_form(
            first_name="Test",
            last_name="User",
            email=Config.VALID_EMAIL
        )

        checkout.accept_terms_and_conditions()
        checkout.click_pay_button()
        checkout.proceed_to_payment_gateway()


        gateway.fill_card_details()
        gateway.click_submit_payment()


        self.page.pause()