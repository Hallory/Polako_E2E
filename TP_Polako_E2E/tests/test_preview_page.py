import pytest

from TP_Polako_E2E.base.base_test import BaseTest
from TP_Polako_E2E.utils.constants import (
    EVENT_COST,
    EVENT_DESCRIPTION,
    EVENT_DURATION,
    EVENT_LOCATION,
    EVENT_NAME,
    IMAGE_PATH,
    TITLE_TEXT_RESULT,
)


class TestPreviewPage(BaseTest):

    @pytest.mark.skip(reason="Test is under development")
    def test_event_preview_content(self):
        self.login_page.login_as_valid_user()
        self.login_page.click_profile()

        self.user_profile.click_profile_btn()
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

        self.event_preview_page.get_title_text()
        self.event_preview_page.is_image_visible()
        self.manager_profile.click_event_management_link()

        assert len(self.event_preview_page.get_title_text()) > 0, TITLE_TEXT_RESULT
        assert (
            self.event_preview_page.is_image_visible()
        ), "The event image is not displaying!"

    @pytest.mark.skip(reason="Test is under development")
    def test_event_preview_content_in_new_window(self):
        self.login_page.login_as_valid_user()
        self.login_page.click_profile()

        self.user_profile.click_profile_btn()

        with self.page.context.expect_page() as new_page_info:
            self.manager_profile.click_event_management_link()
        new_page = new_page_info.value
        new_page.wait_for_load_state()

        events_list_new = self.events_list.__class__(new_page)
        event_preview_new = self.event_preview_page.__class__(new_page)

        events_list_new.create_event_btn_is_visible()
        events_list_new.click_create_event_btn()
        events_list_new.fill_title_field(EVENT_NAME)
        events_list_new.fill_description_field(EVENT_DESCRIPTION)
        events_list_new.select_current_date()
        events_list_new.fill_duration_field(EVENT_DURATION)
        events_list_new.select_category_field()
        events_list_new.select_category_option()
        events_list_new.select_language_field()
        events_list_new.select_language_option()
        events_list_new.select_price_field()
        events_list_new.select_price_type()
        events_list_new.fill_visit_cost_field(EVENT_COST)
        events_list_new.fill_location_field(EVENT_LOCATION)
        events_list_new.upload_image_field(str(IMAGE_PATH))
        events_list_new.click_save_event_btn()

        assert len(event_preview_new.get_title_text()) > 0, TITLE_TEXT_RESULT
        assert (
            event_preview_new.is_image_visible()
        ), "The event image is not displaying!"

        new_page.close()
