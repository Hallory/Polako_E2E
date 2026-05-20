import os

import pytest
from dotenv import load_dotenv

from TP_Polako_E2E.pages.auth.login_page import LoginPage
from TP_Polako_E2E.pages.profile.user_profile_page import UserProfilePage

load_dotenv()


def test_login_success(app_page):
    login_page = LoginPage(app_page)
    user_profile = UserProfilePage(app_page)

    login_page.login_as_valid_user()
    login_page.click_profile()
    user_profile.verify_logout_button_visible()
