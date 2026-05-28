from TP_Polako_E2E.base.base_test import BaseTest


class TestTicketCart(BaseTest):

    def test_add_first_ticket_to_cart(self):
        self.login_page.login_as_valid_user()

        self.events_list.click_active_slider_event()

        self.ticket_selection_page.select_test_ticket()
        self.ticket_selection_page.open_cart()

        self.ticket_selection_page.assert_cart_timer_is_visible()

    def test_add_second_ticket_to_cart(self):
        self.login_page.login_as_valid_user()

        self.events_list.click_active_slider_event()

        self.ticket_selection_page.select_testo123_ticket()
        self.ticket_selection_page.open_cart()

        self.ticket_selection_page.assert_cart_timer_is_visible()

    def test_add_third_ticket_to_cart(self):
        self.login_page.login_as_valid_user()

        self.events_list.click_active_slider_event()

        self.ticket_selection_page.select_test321_ticket()
        self.ticket_selection_page.open_cart()

        self.ticket_selection_page.assert_cart_timer_is_visible()
