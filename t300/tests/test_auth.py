from data.constants import MANAGER_USER


def test_login_form_opens(app):
    app.auth.open_login_form()

    app.auth.should_show_login_form()


def test_sign_button_disabled_by_default(app):
    app.auth.open_login_form()
    
    app.auth.should_have_disabled_submit_button()


def test_sign_in_enabled_after_fill(app):
    app.auth.open_login_form()
    app.auth.fill_login_form(MANAGER_USER["email"], MANAGER_USER["password"])

    app.auth.should_have_enabled_submit_button()


def test_manager_can_login(app):
    app.auth.login(MANAGER_USER["email"], MANAGER_USER["password"])

    app.auth.should_be_logged_in()

