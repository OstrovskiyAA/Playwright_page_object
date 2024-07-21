from playwright.sync_api import Page, expect
from pages.base_page import BasePage
BUTTON = "#submit-id-submit"
RESULT= ".result-text"
class SimplePage(BasePage):
    url = "https://www.qa-practice.com/elements/button/simple"
    def check_button_exists(self):
        result = self.page.locator(BUTTON)
        expect(result).to_be_visible()
    def click_button(self):
        result = self.page.locator(BUTTON)
        result.click()
    def check_result_text_is_(self, text):
        expect(self.page.locator(RESULT)).to_have_text(text)