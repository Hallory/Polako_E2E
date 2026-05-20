from TP_Polako_E2E.base.base_page import BasePage


class ContractsPage(BasePage):
    CONTRACT_ITEM = ".contract-row"
    CONTRACT_STATUS = ".contract-status__label"
    VIEW_DETAILS_BTN = 'a[href*="/contracts/details"]'

    def get_contracts_count(self) -> int:
        return self.page.locator(self.CONTRACT_ITEM).count()

    def open_contract_by_index(self, index: int = 0):
        self.page.locator(self.VIEW_DETAILS_BTN).nth(index).click()

    def get_contract_status(self, index: int = 0) -> str:
        return (
            self.page.locator(self.CONTRACT_STATUS)
            .nth(index)
            .get_attribute("data-status")
        )
