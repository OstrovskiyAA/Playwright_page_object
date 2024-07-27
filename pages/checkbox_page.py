from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckBox(BasePage):
    url = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    def fill_checkbox(self):
        self.page.get_by_role("checkbox", name="Select me or not").click()
        self.page.locator("css=[name='submit']").click()
    def assert_checkbox(self, text):
        expect(self.page.locator('css=[class=result-text]')).to_have_text(text)