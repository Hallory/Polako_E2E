
def test_account_sidebar_links_are_visible(manager_app):
    manager_app.auth.open_profile()
    manager_app.sidebar.should_have_main_links()
    
    
