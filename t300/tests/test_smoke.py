def test_open_site(app):
    assert "Polako" in app.events.get_title()