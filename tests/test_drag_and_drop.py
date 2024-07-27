from playwright.sync_api import Page
def test_drag_and_drop(page: Page):
    page.goto('https://demoqa.com/droppable')
    drag = page.locator('#draggable')
    drop = page.locator('#droppable')
    page.drag_and_drop('#draggable','#droppable')
    page.screenshot(type='jpeg', path='C:/Users/Алексей/PycharmProjects/Playwright_page_object/drag.jpg')