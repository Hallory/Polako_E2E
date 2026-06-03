import re
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_sidebar_profile_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.profile_link).to_have_attribute(
        "href", re.compile(auth_profile_app.profile.URL)
    )


@pytest.mark.regression
def test_sidebar_purchases_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.purchases_link).to_have_attribute(
        "href", re.compile("purchases")
    )


@pytest.mark.regression
def test_sidebar_company_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.company_link).to_have_attribute(
        "href", re.compile("company-settings")
    )


@pytest.mark.regression
def test_sidebar_manage_events_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.manage_events_link).to_have_attribute(
        "href", re.compile("events")
    )


@pytest.mark.regression
def test_sidebar_contracts_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.contracts_link).to_have_attribute(
        "href", re.compile(r"/user/contracts$")
    )


@pytest.mark.regression
def test_sidebar_reports_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.reports_link).to_have_attribute(
        "href", re.compile("reports")
    )


@pytest.mark.regression
def test_sidebar_qr_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.create_qr_link).to_have_attribute(
        "href", re.compile("qr-generator")
    )


@pytest.mark.regression
def test_sidebar_withdrawal_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.withdrawal_link).to_have_attribute(
        "href", re.compile("withdrawal")
    )


@pytest.mark.regression
def test_sidebar_contract_data_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.contract_data_link).to_have_attribute(
        "href", re.compile("contract-data")
    )


@pytest.mark.regression
def test_sidebar_management_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.management_link).to_have_attribute(
        "href", re.compile("management")
    )


@pytest.mark.regression
def test_sidebar_publications_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.publication_link).to_have_attribute(
        "href", re.compile("publications")
    )


@pytest.mark.regression
def test_sidebar_balance_link_has_correct_route(auth_profile_app):
    expect(auth_profile_app.sidebar.balance_link).to_have_attribute(
        "href", re.compile("balance")
    )
