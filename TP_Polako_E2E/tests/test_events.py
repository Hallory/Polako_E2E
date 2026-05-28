import pytest

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.utils.constants import (
    EVENT_COST,
    EVENT_DESCRIPTION,
    EVENT_DURATION,
    EVENT_LOCATION,
    EVENT_NAME,
    IMAGE_PATH,
)


class TestEvent(BaseTest):

    @pytest.mark.skip(reason="Test is under development")
    def test_create_event_button_is_clickable(self):
        self.login_page.login_and_go_to_profile()

        self.manager_profile.force_click_event_management_link()

        self.events_list.create_event_btn_is_visible()
        self.events_list.click_create_event_btn()

    @pytest.mark.skip(reason="Test is under development")
    def test_create_event(self):
        self.login_page.login_as_valid_user()
        self.login_page.click_profile()

        self.manager_profile.force_click_event_management_link()
        self.events_list.create_event_btn_is_visible()
        self.events_list.click_create_event_btn()

        self.events_list.fill_title_field(EVENT_NAME)
        self.events_list.fill_description_field(EVENT_DESCRIPTION)

        self.events_list.select_current_date()
        self.events_list.fill_duration_field(EVENT_DURATION)

        self.events_list.select_category_field()
        self.events_list.select_category_option()

        self.events_list.select_language_field()
        self.events_list.select_language_option()

        self.events_list.select_price_field()
        self.events_list.select_price_type()

        self.events_list.fill_visit_cost_field(EVENT_COST)
        self.events_list.fill_location_field(EVENT_LOCATION)

        self.events_list.upload_image_field(str(IMAGE_PATH))

        self.events_list.click_save_event_btn()
