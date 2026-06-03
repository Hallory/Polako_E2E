from pages.purchases.purchases_page import PurchasePage
from pages.auth.auth_page import AuthPage
from pages.components.account_sidebar import AccountSidebar
from pages.profile.personal_information_page import PersonalInformationPage
from pages.events.events_page import EventsPage
from pages.events.create_event_page import CreateEventPage
from pages.events.edit_event_page import EditEventPage
from pages.company.company_page import CompanyPage
from pages.contracts.contracts_page import ContractsPage
from pages.contracts.contract_data_page import ContractDataPage
from pages.reports.reports_page import ReportsPage
from pages.withdrawal.withdrawal_page import WithdrawalPage
from pages.events.event_actions_component import EventActionsComponent
from pages.events.event_preview_page import EventPreviewPage
from pages.events.tickets_page import TicketsPage
from pages.events.tickets_with_seats_page import TicketsWithSeatsPage
from pages.create_qr.create_qr_page import CreateQrPage


class App:
    def __init__(self, page):
        self.page = page
        self.auth = AuthPage(page)
        self.sidebar = AccountSidebar(page)
        self.profile = PersonalInformationPage(page)
        self.purchases = PurchasePage(page)
        self.events = EventsPage(page)
        self.create_event = CreateEventPage(page)
        self.edit_event = EditEventPage(page)
        self.company = CompanyPage(page)
        self.contracts = ContractsPage(page)
        self.contract_data = ContractDataPage(page)
        self.reports = ReportsPage(page)
        self.withdrawal = WithdrawalPage(page)
        self.event_actions = EventActionsComponent(page)
        self.event_preview = EventPreviewPage(page)
        self.tickets = TicketsPage(page)
        self.tickets_with_seats = TicketsWithSeatsPage(page)
        self.create_qr = CreateQrPage(page)