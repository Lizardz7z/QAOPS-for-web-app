import conftest
from selectrs.locators import selectors_cart_page, selectors_products_page
import pytest
import allure

browsers = ['setup_browser_chrome', 'setup_browser_firefox', 'setup_browser_webkit']

@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Check goods adding to the cart")
@allure.story("Проверка функции добавления товаров в корзину")
def test_add_to_cart(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        our_products = {
            products[i].get_attribute(
                selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper(): 0
                        for i in range(len(products))}
        for i in range(len(products)):
            products[i].click()
            our_products[
                products[i].get_attribute(
                    selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
            page.wait_for_timeout(2000)
            close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
            close_button.click()
            page.wait_for_timeout(1000)
        products[3].click()
        our_products[
            products[3].get_attribute(
                selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
        products_in_cart = page.query_selector_all(selectors_cart_page.ITEMS_IN_CART)
        products_names_in_cart = {}
    with allure.step("Проверка правильности добавления товаров"):
        for i in range(len(products_in_cart)):
            products_names_in_cart[
                products_in_cart[i].query_selector(
                    selectors_cart_page.PRODUCT_NAME).inner_text()] = \
                int(products_in_cart[i].query_selector(selectors_cart_page.QUANTITY).inner_text())
        for i in our_products.items():
            assert products_names_in_cart[i[0]] == i[1], \
                "Products added to cart incorrectly"
