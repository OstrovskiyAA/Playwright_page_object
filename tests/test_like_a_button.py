from playwright.sync_api import Page, expect

from pages.like_a_button_page import ButtonPage


def test_buttom_exists(page:Page):
    button_page=ButtonPage(page)
    button_page.open()
    button_page.check_button_exists()

def test_buttom_click(page:Page):
    button_page=ButtonPage(page)
    button_page.open()
    button_page.click_button()
    button_page.check_have_exact_text_("Submitted")