from playwright.sync_api import sync_playwright

import locators
from tests import test_navigation_menu
from tests import test_cart_functionality


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(locators.Selectors.PAGE_LINK)

        test_navigation_menu.test_go_to_home_page(page)
        test_navigation_menu.test_go_to_products_page(page)
        test_cart_functionality.add_to_cart(page)
        test_cart_functionality.check_prices(page)

        browser.close()


if __name__ == '__main__':
    main()
