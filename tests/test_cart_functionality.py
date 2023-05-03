from selectrs.locators import selectors_cart_page, selectors_products_page
import pytest
import allure


@allure.feature("Cart functionality checking")
@pytest.mark.slow
@allure.feature("Check goods adding to the cart")
@allure.story("Проверка функции добавления товаров в корзину")
def test_add_to_cart(setup_browser):
    with allure.step("Запуск браузера и открытие страницы"):
        page = setup_browser
    with allure.step("Переход на страницу 'продукты'"):
        link = page.query_selector(selectors_products_page.PRODUCTS_PAGE_LINK)
        link.click()
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
