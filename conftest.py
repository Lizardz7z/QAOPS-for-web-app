import pytest
from playwright.sync_api import sync_playwright

from selectrs.locators import selectors_base_page


@pytest.fixture(scope="function")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(selectors_base_page.PAGE_LINK)
        yield page
        browser.close()


