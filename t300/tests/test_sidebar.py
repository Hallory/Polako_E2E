
from playwright.sync_api import expect


def test_account_sidebar_links_are_visible(manager_app):
    manager_app.profile.open()

    expect(manager_app.sidebar.sidebar).to_be_visible()
    expect(manager_app.sidebar.profile_link).to_be_visible()
    expect(manager_app.sidebar.purchases_link).to_be_visible()
    expect(manager_app.sidebar.company_link).to_be_visible()
    expect(manager_app.sidebar.manage_events_link).to_be_visible()
    expect(manager_app.sidebar.contracts_link).to_be_visible()
    expect(manager_app.sidebar.reports_link).to_be_visible()
    expect(manager_app.sidebar.create_qr_link).to_be_visible()
    expect(manager_app.sidebar.withdrawal_link).to_be_visible()
