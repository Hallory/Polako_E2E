from TP_Polako_E2E.base.base_page import BasePage

EXIT_BTN = "//button[@type='button' and @data-slot='button']"
EVENT_MNG_BTN = 'a[href="/ru/user/events"]'


class UserProfilePage(BasePage):
    def verify_logout_button_visible(self):
        self.verify_element_is_visible(selector=EXIT_BTN, element_name="Logout Button")

    def click_event_management_link(self):
        self.page.click(EVENT_MNG_BTN)
