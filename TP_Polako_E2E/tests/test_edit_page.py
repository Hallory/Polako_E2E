from tests.test_events import image_path

from TP_Polako_E2E.base.base_test import BaseTest


class TestEditEvent(BaseTest):
    def test_edit_event(self):
        self.login_page.login_as_valid_user()
        self.login_page.click_profile()
        self.user_profile.click_event_management_link()
        self.events_list.create_event_btn_is_visible()
        self.events_list.click_create_event_btn()
        self.events_list.fill_title_field("test_event")
        self.events_list.fill_description_field("test_description")
        self.events_list.select_current_date()
        self.events_list.fill_duration_field("60")
        self.events_list.select_category_field()
        self.events_list.select_category_option()
        self.events_list.select_language_field()
        self.events_list.select_language_option()
        self.events_list.select_price_field()
        self.events_list.select_price_type()
        self.events_list.fill_visit_cost_field("100")
        self.events_list.fill_location_field("Test Location (NS)")
        self.events_list.upload_image_field(str(image_path))
        self.events_list.click_save_event_btn()

        self.event_edit_page.get_page_title()
        self.event_edit_page.click_save_event_btn()

        assert (
            len(self.event_edit_page.get_page_title()) > 0
        ), "The event title is empty."
