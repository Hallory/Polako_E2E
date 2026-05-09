

def test_manager_can_open_profile_page(manager_app):
    manager_app.auth.open_profile()
    
    manager_app.profile.should_be_on_profile_page()