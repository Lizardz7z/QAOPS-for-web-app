from playwright.sync_api import sync_playwright

import selectors
from tests import test_navigation_menu
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page=browser.new_page()
        page.goto(selectors.Selectors.PAGE_LINK)

        test_navigation_menu.test_go_to_home_page(page)
        test_navigation_menu.test_go_to_products_page(page)

        browser.close()

if __name__=='__main__':
    main()