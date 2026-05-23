import os
from urllib.parse import urlparse

import pytest

from TP_Polako_E2E.pages.auth.login_page import LoginPage
from TP_Polako_E2E.pages.common.header import HeaderPage
from TP_Polako_E2E.pages.events.event_edit_page import EventEditPage
from TP_Polako_E2E.pages.events.event_management_page import EventManagementPage
from TP_Polako_E2E.pages.events.event_preview_page import EventPreviewPage
from TP_Polako_E2E.pages.events.events_list_page import EventsListPage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage


class BaseTest:
    login_page: LoginPage
    user_profile: UserProfilePage
    events_list: EventsListPage
    api_token: str
    header_page: HeaderPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, app_page, authorized_profile_api, api_auth_token):
        self.page = app_page
        self.login_page = LoginPage(app_page)
        self.user_profile = UserProfilePage(app_page)
        self.events_list = EventsListPage(app_page)
        self.profile_api = authorized_profile_api
        self.api_token = api_auth_token
        self.header_page = HeaderPage(app_page)
        self.event_preview_page = EventPreviewPage(app_page)
        self.event_edit_page = EventEditPage(app_page)
        self.event_management_page = EventManagementPage(app_page)

    def authenticate_via_token(self) -> UserProfilePage:
        raw_url = os.getenv("STG_URL")
        parsed = urlparse(raw_url)
        clean_base_url = f"{parsed.scheme}://{parsed.netloc}"
        domain = parsed.netloc

        self.page.context.add_cookies(
            [
                {
                    "name": "access_token",
                    "value": self.api_token,
                    "domain": domain,
                    "path": "/",
                }
            ]
        )

        self.page.goto(f"{clean_base_url}/ru/user/personal-information")
        self.page.wait_for_load_state("networkidle")

        return self.user_profile
        self.event_edit_page = EventEditPage(app_page)
        self.event_preview_page = EventPreviewPage(app_page)
        self.event_management_page = EventManagementPage(app_page)
        self.header_page = HeaderPage(app_page)
