from playwright.sync_api import Page, expect

from pages.checkbox_page import CheckBox

def test_check_box(page:Page):
    check_box = CheckBox(page)
    check_box.open()
    check_box.fill_checkbox()
    check_box.assert_checkbox()


