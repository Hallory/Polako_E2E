from TP_Polako_E2E.base.base_page import BasePage

DOWNLOAD_QR_BTN = 'button[data-action="download-qr"]'
QR_IMAGE_CONTAINER = ".qr-code-viewer img"
REFRESH_QR_BTN = "button.refresh-code"


class QrCodePage(BasePage):

    def download_qr_code(self):
        with self.page.expect_download() as download_info:
            self.click(self.DOWNLOAD_QR_BTN)
        return download_info.value

    def is_qr_visible(self) -> bool:
        return self.is_visible(self.QR_IMAGE_CONTAINER)
