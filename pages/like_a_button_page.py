from playwright.sync_api import Page, expect
from pages.base_page import BasePage
BUTTON= ".a-button"
RESULT= ".result-text"

class ButtonPage(BasePage):
    url="https://www.qa-practice.com/elements/button/like_a_button"
    def check_button_exists(self):
        result = self.page.locator(BUTTON)
        expect(result).to_be_visible()

    def click_button(self):
        self.page.locator(BUTTON).click()

    def check_have_exact_text_(self, text):
        expect(self.page.locator(RESULT)).to_have_text(text)