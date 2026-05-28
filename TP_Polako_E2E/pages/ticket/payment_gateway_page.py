from TP_Polako_E2E.base.base_page import BasePage
from TP_Polako_E2E.utils.config import Config


class PaymentGatewayPage(BasePage):
    _CARD_NUMBER_INPUT = "#pan"
    _EXPIRY_MONTH_SELECT = "#Ecom_Payment_Card_ExpDate_Month"
    _EXPIRY_YEAR_SELECT = "#Ecom_Payment_Card_ExpDate_Year"
    _CVV_INPUT = "#cv2"
    _SUBMIT_PAYMENT_BUTTON = "#pay"

    def fill_card_details(self):

        self.page.wait_for_selector(
            self._CARD_NUMBER_INPUT, timeout=45000, state="visible"
        )

        self.fill(self._CARD_NUMBER_INPUT, Config.CARD_NUMBER)

        self.page.select_option(self._EXPIRY_MONTH_SELECT, Config.EXP_MONTH)
        self.page.select_option(self._EXPIRY_YEAR_SELECT, Config.EXP_YEAR)

        self.fill(self._CVV_INPUT, Config.SVV_CODE)

    def click_submit_payment(self):

        self.click(self._SUBMIT_PAYMENT_BUTTON)
