from TP_Polako_E2E.base.base_page import BasePage

PREVIEW_TITLE = "article h1"
PREVIEW_IMAGE = "article img"


class EventPreviewPage(BasePage):

    def get_title_text(self) -> str:
        return self.page.locator(PREVIEW_TITLE).inner_text()

    def is_image_visible(self) -> bool:
        return self.page.locator(PREVIEW_IMAGE).first.is_visible()
