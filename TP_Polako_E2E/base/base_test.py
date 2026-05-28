import pytest

from TP_Polako_E2E.pages.auth.forgot_password_page import ForgotPasswordPage
from TP_Polako_E2E.pages.auth.login_page import LoginPage
from TP_Polako_E2E.pages.auth.registration_page import RegistrationPage
from TP_Polako_E2E.pages.common.header import HeaderPage
from TP_Polako_E2E.pages.events.event_edit_page import EventEditPage
from TP_Polako_E2E.pages.events.event_management_page import EventManagementPage
from TP_Polako_E2E.pages.events.event_preview_page import EventPreviewPage
from TP_Polako_E2E.pages.events.events_list_page import EventsListPage
from TP_Polako_E2E.pages.profile.manager_profile_page import ManagerProfilePage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage
from TP_Polako_E2E.pages.ticket.checkout_page import CheckoutPage
from TP_Polako_E2E.pages.ticket.payment_gateway_page import PaymentGatewayPage
from TP_Polako_E2E.pages.ticket.ticket_selection_page import TicketSelectionPage


class BaseTest:
    login_page: LoginPage
    user_profile: UserProfilePage
    events_list: EventsListPage
    header_page: HeaderPage
    forgot_password_page: ForgotPasswordPage
    registration_page: RegistrationPage
    manager_profile: ManagerProfilePage
    page = None
    event_preview_page: EventPreviewPage
    event_edit_page: EventEditPage
    event_management_page: EventManagementPage
    ticket_selection_page: TicketSelectionPage
    checkout_page: CheckoutPage
    payment_gateway_page: PaymentGatewayPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, app_page):
        self.page = app_page
        self.login_page = LoginPage(app_page)
        self.user_profile = UserProfilePage(app_page)
        self.events_list = EventsListPage(app_page)
        self.header_page = HeaderPage(app_page)
        self.event_preview_page = EventPreviewPage(app_page)
        self.event_edit_page = EventEditPage(app_page)
        self.event_management_page = EventManagementPage(app_page)
        self.forgot_password_page = ForgotPasswordPage(app_page)
        self.registration_page = RegistrationPage(app_page)
        self.manager_profile = ManagerProfilePage(app_page)
        self.ticket_selection_page = TicketSelectionPage(app_page)
        self.checkout_page = CheckoutPage(app_page)
        self.payment_gateway_page = PaymentGatewayPage(app_page)


class BaseManagerTest(BaseTest):
    @pytest.fixture(autouse=True)
    def auto_manager_login(self, setup_pages, manager_page):
        self.page = manager_page


class BaseUserTest(BaseTest):
    @pytest.fixture(autouse=True)
    def auto_user_login(self, setup_pages, user_page):
        self.page = user_page