from TP_Polako_E2E.pages.auth.login_page import LoginPage
from TP_Polako_E2E.pages.events.events_list_page import EventsListPage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage



def test_create_event_button_is_clickable(app_page):
    login = LoginPage(app_page)
    user_profile = UserProfilePage(app_page)
    events_list = EventsListPage(app_page)

    login.login_as_valid_user()
    login.click_profile()
    user_profile.click_event_management_link()

    events_list.create_event_btn_is_visible()
    events_list.click_create_event_btn()
