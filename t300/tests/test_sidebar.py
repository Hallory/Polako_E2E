import re
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_sidebar_navigate_to_profile(auth_profile_app):
    auth_profile_app.sidebar.open_profile()
    expect(auth_profile_app.page).to_have_url(re.compile(auth_profile_app.profile.URL))


@pytest.mark.regression
def test_sidebar_navigate_to_purchases(auth_profile_app):
    auth_profile_app.sidebar.open_purchases()
    expect(auth_profile_app.page).to_have_url(re.compile("purchases"))


@pytest.mark.regression
def test_sidebar_navigate_to_company(auth_profile_app):
    auth_profile_app.sidebar.open_company()
    expect(auth_profile_app.page).to_have_url(re.compile("company-settings"))


@pytest.mark.regression
def test_sidebar_navigate_to_manage_events(auth_profile_app):
    auth_profile_app.sidebar.open_manage_events()
    expect(auth_profile_app.page).to_have_url(re.compile("events"))


@pytest.mark.regression
def test_sidebar_navigate_to_contracts(auth_profile_app):
    auth_profile_app.sidebar.open_contracts()
    expect(auth_profile_app.page).to_have_url(re.compile("contracts"))


@pytest.mark.regression
def test_sidebar_navigate_to_reports(auth_profile_app):
    auth_profile_app.sidebar.open_reports()
    expect(auth_profile_app.page).to_have_url(re.compile("reports"))


@pytest.mark.regression
def test_sidebar_navigate_to_qr(auth_profile_app):
    auth_profile_app.sidebar.open_create_qr()
    expect(auth_profile_app.page).to_have_url(re.compile("qr-generator"))


@pytest.mark.regression
def test_sidebar_navigate_to_withdrawal(auth_profile_app):
    auth_profile_app.sidebar.open_withdrawal()
    expect(auth_profile_app.page).to_have_url(re.compile("withdrawal"))


@pytest.mark.regression
def test_sidebar_navigate_to_contract_data(auth_profile_app):
    auth_profile_app.sidebar.open_contract_data()
    expect(auth_profile_app.page).to_have_url(re.compile("contract-data"))


@pytest.mark.regression
def test_sidebar_navigate_to_management(auth_profile_app):
    auth_profile_app.sidebar.open_management()
    expect(auth_profile_app.page).to_have_url(re.compile("management"))


@pytest.mark.regression
def test_sidebar_navigate_to_publications(auth_profile_app):
    auth_profile_app.sidebar.open_publication()
    expect(auth_profile_app.page).to_have_url(re.compile("publications"))


@pytest.mark.regression
def test_sidebar_navigate_to_balance(auth_profile_app):
    auth_profile_app.sidebar.open_balance()
    expect(auth_profile_app.page).to_have_url(re.compile("balance"))
