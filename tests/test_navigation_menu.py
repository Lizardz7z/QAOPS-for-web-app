from selectrs.locators import *
from POM import BasePage


def test_go_to_home_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_base_page.HOME_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_base_page.HOME_PAGE_TITLE)
    assert title.inner_text() == "IMPRESSO ESPRESSO", "Link to home page is not working"
    close_browser(browser)


def test_go_to_our_menu_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_menu_page.OUR_MENU_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_menu_page.OUR_MENU_PAGE_TITLE)
    assert title.inner_text() == "OUR MENU", "Link to our menu page is not working"
    close_browser(browser)


def test_go_to_products_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_products_page.PRODUCTS_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_products_page.PRODUCTS_PAGE_TITLE)
    assert title.inner_text() == "PRODUCTS", "Link to products page is not working"
    close_browser(browser)


def test_go_to_about_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_about_page.ABOUT_PAGE_TITLE)
    assert title.inner_text() == "ABOUT US", "Link to home page is not working"
    close_browser(browser)


def test_go_to_contactus_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_TITLE)
    assert title.inner_text() == "CONTACT US", "Link to home page is not working"
    close_browser(browser)


def test_go_to_cart_page(setup_browser, close_browser):
    page, browser = setup_browser()
    link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(selectors_cart_page.CART_PAGE_TITLE)
    assert title.inner_text() == "MY CART", "Link to home page is not working"
    close_browser(browser)

