from locators import Selectors


def add_to_cart(page):
    products = page.query_selector_all(Selectors.ITEMS_SELECTOR)
    close_button = page.query_selector(Selectors.CART_CLOSE_BUTTON)
    our_products = {products[i].get_attribute(Selectors.DATA_ITEM_NAME_ATTRIBUTE).upper(): 0
                    for i in range(len(products))}
    for i in range(len(products)):
        products[i].click()
        our_products[products[i].get_attribute(Selectors.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
        page.wait_for_timeout(2000)
        close_button.click()
        page.wait_for_timeout(1000)
    products[3].click()
    our_products[products[3].get_attribute(Selectors.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
    cart_link = page.query_selector(Selectors.CART_PAGE_LINK)
    cart_link.click()
    page.wait_for_timeout(2000)
    products_in_cart = page.query_selector_all(Selectors.ITEMS_IN_CART)
    products_names_in_cart = {}
    for i in range(len(products_in_cart)):
        products_names_in_cart[products_in_cart[i].query_selector(Selectors.PRODUCT_NAME).inner_text()] = \
            int(products_in_cart[i].query_selector(Selectors.QUANTITY).inner_text())
    for i in our_products.items():
        assert products_names_in_cart[i[0]] == i[1], "Products added to cart incorrectly"


def check_prices(page):
    prices = page.query_selector_all(Selectors.ITEMS_IN_CART)
    prices_home = page.query_selector_all(Selectors.ITEMS_SELECTOR)
    page.wait_for_timeout(2000)
    our_products = {prices_home[i].get_attribute(Selectors.DATA_ITEM_NAME_ATTRIBUTE).upper():
                    float(prices_home[i].get_attribute(Selectors.DATA_ITEM_PRICE_ATTRIBUTE))
                    for i in range(len(prices_home))}
    subtotal = 0.0
    for i in range(len(prices)):
        total = prices[i].query_selector(Selectors.UNIT_PRICE)
        total = float(total.inner_text()[1:])
        assert total == our_products[prices[i].query_selector(Selectors.PRODUCT_NAME).inner_text()], \
            "The price calculated incorrectly"
        total *= int(prices[i].query_selector(Selectors.QUANTITY).inner_text())
        total_price = prices[i].query_selector(Selectors.TOTAL_PRICE).inner_text()[1:]
        assert total == float(total_price), "The total price calculated incorrectly"
        subtotal += float(total)
    sum_of_products = page.query_selector(Selectors.SUM_OF_PRODUCTS)
    s1 = sum_of_products.inner_text()
    s1 = float(s1[1:])
    assert s1 == subtotal, "The subtotal price calculated incorrectly"
