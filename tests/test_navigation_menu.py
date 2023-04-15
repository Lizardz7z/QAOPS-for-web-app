from locators import Selectors


def test_go_to_home_page(page):
    link = page.query_selector(Selectors.HOME_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.HOME_PAGE_TITLE)
    assert title.inner_text() == "IMPRESSO ESPRESSO", "Link to home page is not working"


def test_go_to_our_menu_page(page):
    link = page.query_selector(Selectors.OUR_MENU_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.OUR_MENU_PAGE_TITLE)
    assert title.inner_text() == "OUR MENU", "Link to our menu page is not working"


def test_go_to_products_page(page):
    link = page.query_selector(Selectors.PRODUCTS_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.PRODUCTS_PAGE_TITLE)
    assert title.inner_text() == "PRODUCTS", "Link to products page is not working"


def test_go_to_about_page(page):
    link = page.query_selector(Selectors.ABOUT_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.ABOUT_PAGE_TITLE)
    assert title.inner_text() == "ABOUT US", "Link to home page is not working"


def test_go_to_contactus_page(page):
    link = page.query_selector(Selectors.CONTACTUS_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.CONTACTUS_PAGE_TITLE)
    assert title.inner_text() == "CONTACT US", "Link to home page is not working"


def test_go_to_cart_page(page):
    link = page.query_selector(Selectors.CART_PAGE_LINK)
    link.click()
    page.wait_for_timeout(2000)
    title = page.query_selector(Selectors.CART_PAGE_TITLE)
    assert title.inner_text() == "MY CART", "Link to home page is not working"

