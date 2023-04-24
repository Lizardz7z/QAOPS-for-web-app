import pytest
from playwright.sync_api import sync_playwright

PAGE_LINK = 'https://impresso-expresso.netlify.app/'


@pytest.fixture
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(PAGE_LINK)
        return page, browser


@pytest.fixture
def close_browser(browser):
    browser.close()