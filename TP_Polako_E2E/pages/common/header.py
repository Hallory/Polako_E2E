from TP_Polako_E2E.base.base_page import BasePage

HEADER_LOGO = 'header img[alt="logo"]'
HEADER_CART_BTN = 'header button[aria-label="Cart"]'
LANG_DROPDOWN_BTN = 'header [data-testid$="select-language"]'

LANG_OPTIONS = {
    "en": 'header span:has-text("English")',
    "ru": 'header span:has-text("Русский")',
    "sr": 'header span:has-text("Srpski")',
}

LOGIN_MODAL_OPEN_BTN = 'header button:has-text("Войти")'
PROFILE_BTN = "header div.xl\\:flex > a"

NAV_LINKS = {
    "events": 'header nav a[href*="#events"]',
    "prices": 'header nav a[href*="pricing"]',
    "tickets": 'header nav a[href*="polako-tickets"]',
    "certificates": 'header nav a[href*="services"]',
    "news": 'header nav a[href*="news"]',
    "about": 'header nav a[href*="about"]',
    "analytics": 'header nav a[href*="analytics"]',
}

CONTACTS_DROPDOWN_BTN = "header div.xl\\:flex > div:nth-child(1) button"
CONTACTS_MENU_CONTAINER = "header div.xl\\:flex > div:nth-child(1) > ul"

CONTACT_LINKS = {
    "telegram": 'header a[href*="t.me"]',
    "instagram_ru": 'header a:has-text("Instagram RU")',
    "instagram_sr": 'header a:has-text("Instagram SR")',
    "email": 'header a[href^="mailto:"]',
    "viber": 'header a[href*="viber"]',
    "whatsapp": 'header a[href*="whatsapp.com"]',
}

CART_DRAWER = "div.slide-in-from-right"


class HeaderPage(BasePage):

    # LOGO
    def click_logo(self):
        self.page.locator(HEADER_LOGO).click()

    def verify_logo_visible(self):
        self.page.locator(HEADER_LOGO).wait_for(state="visible", timeout=5000)

    # Lokalization
    def open_language_dropdown(self):
        self.page.locator(LANG_DROPDOWN_BTN).click()

    def change_language(self, lang_code: str):
        self.open_language_dropdown()
        selector = LANG_OPTIONS[lang_code.lower()]
        self.page.locator(selector).click()

    def get_current_language_text(self) -> str:
        return self.page.locator(LANG_DROPDOWN_BTN).inner_text().strip()

    # Autorization and Profile
    def open_login_modal(self):
        self.page.locator(LOGIN_MODAL_OPEN_BTN).click(force=True)

    def click_profile(self):
        self.page.locator(PROFILE_BTN).click()

    def verify_login_button_visible(self):
        self.page.locator(LOGIN_MODAL_OPEN_BTN).wait_for(state="visible", timeout=5000)

    def verify_profile_button_visible(self):
        self.page.locator(PROFILE_BTN).wait_for(state="visible", timeout=5000)

    # Navigation and Cart
    def click_nav_link(self, key_name: str):
        selector = NAV_LINKS[key_name.lower()]
        self.page.locator(selector).click()

    def verify_nav_link_visible(self, key_name: str):
        selector = NAV_LINKS[key_name.lower()]
        self.page.locator(selector).wait_for(state="visible", timeout=3000)

    def click_cart(self):
        self.page.locator(HEADER_CART_BTN).filter(visible=True).click()

    def get_cart_drawer_locator(self):
        return self.page.locator(CART_DRAWER)

    # Contacts
    def open_contacts_dropdown(self):
        self.page.locator(CONTACTS_DROPDOWN_BTN).click()
        self.page.locator(CONTACTS_MENU_CONTAINER).wait_for(
            state="visible", timeout=3000
        )

    def get_contact_href(self, platform_name: str) -> str:

        selector = CONTACT_LINKS[platform_name.lower()]
        return self.page.locator(selector).get_attribute("href")
