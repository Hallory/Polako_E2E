from TP_Polako_E2E.base.base_page import BasePage

ADD_DATA_BTN = "button.bg-primary-500"
GO_TO_CONTRACTS_BTN = "a[href*='contracts']"
CONTRACT_DATA_ITEM = "div.flex.flex-col.gap-1"
ITEM_TITLE = "p.text-base.font-bold"
ITEM_EMAIL = "p.text-xs.text-gray-500"
PAGE_HEADER = "h1.text-2xl"


class ContactDataPage(BasePage):
    def click_add_data(self):
        self.click(ADD_DATA_BTN)

    def click_go_to_contracts(self):
        self.click(GO_TO_CONTRACTS_BTN)

    def get_all_entities_titles(self) -> list[str]:
        return self.page.locator(ITEM_TITLE).all_inner_texts()

    def get_entity_email_by_index(self, index: int = 0) -> str:
        return self.page.locator(ITEM_EMAIL).nth(index).inner_text()

    def open_entity_details_by_title(self, title: str):
        self.page.locator(CONTRACT_DATA_ITEM).filter(
            has=self.page.locator(ITEM_TITLE, has_text=title)
        ).click()

    def is_page_header_visible(self) -> bool:
        return self.is_visible(PAGE_HEADER)
