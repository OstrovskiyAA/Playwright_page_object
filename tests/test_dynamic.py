import time

from playwright.sync_api import Page
import os
def test_dynamic(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.get_by_role("button",name='Visible After 5 Seconds')
    button.click(timeout=7000)
    page.screenshot(type='jpeg', path='C:/Users/Алексей/PycharmProjects/Playwright_page_object/image.jpg')