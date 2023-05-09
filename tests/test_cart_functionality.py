import re
from selectrs.locators import selectors_cart_page, selectors_products_page, \
    selectors_billing_address
import pytest
import allure

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


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


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Check prices in cart")
@allure.story("Проверка подсчета стоимости товаров в корзине")
def test_check_prices(setup_browser, request):
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
    with allure.step("Проверка подсчитанной стоимости"):
        prices = page.query_selector_all(selectors_cart_page.ITEMS_IN_CART)
        prices_home = page.query_selector_all(selectors_cart_page.ITEMS_SELECTOR)
        page.wait_for_timeout(2000)
        our_products = {prices_home[i].get_attribute(
            selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper():
            float(prices_home[i].get_attribute(selectors_cart_page.DATA_ITEM_PRICE_ATTRIBUTE))
            for i in range(len(prices_home))}
        subtotal = 0.0
        for i in range(len(prices)):
            total = prices[i].query_selector(selectors_cart_page.UNIT_PRICE)
            total = float(total.inner_text()[1:])
            assert total == our_products[prices[i].query_selector(
                selectors_cart_page.PRODUCT_NAME).inner_text()], \
                "The price calculated incorrectly"
            total *= int(prices[i].query_selector(selectors_cart_page.QUANTITY).inner_text())
            total_price = prices[i].query_selector(selectors_cart_page.TOTAL_PRICE).inner_text()[1:]
            assert total == float(total_price), "The total price calculated incorrectly"
            subtotal += float(total)
        sum_of_products = page.query_selector(selectors_cart_page.SUM_OF_PRODUCTS)
        s1 = sum_of_products.inner_text()
        s1 = float(s1[1:])
        assert s1 == subtotal, "The subtotal price calculated incorrectly"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking for empty fields")
@allure.story("Проверка пустых полей")
def test_check_empty_fields(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка пустого имени"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^NameThis field is required$")), "No empty name handling"
    with allure.step("Проверка пустого адреса"):
        assert page.locator("div").filter(has_text=re.compile(
            r"^StreetAddressThis field is required$")), \
            "No empty street address handling"
    with allure.step("Проверка пустого города"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^CityThis field is required$")), "No empty city handling"
    with allure.step("Проверка пустого индекса"):
        assert page.locator("div").filter(has_text=re.compile(
            r"^ZIP / Postal codeThis field is required$")), \
            "No empty zip handling"
    with allure.step("Проверка пустого почтового адреса"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^EmailThis field is required$")), "No empty email handling"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a name")
@allure.story("Проверка ввода имени")
def test_check_name(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод имени"):
        name_field = page.query_selector(selectors_billing_address.NAME)
        name_field.fill("Lisa and Masha")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.NAME) == "Lisa and Masha", \
            "Name cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a company name")
@allure.story("Проверка ввода названия компании")
def test_check_company_name(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод названия компании"):
        company_name_field = page.query_selector(selectors_billing_address.COMPANY)
        company_name_field.fill("HSE")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.COMPANY) == 'HSE', \
            "Name cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a street address")
@allure.story("Проверка ввода адреса 1")
def test_check_street_address(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод адреса 1"):
        street_address_field = page.query_selector(selectors_billing_address.ADDRESS1)
        street_address_field.fill("Lvovskaya 1v")
        page.wait_for_timeout(2000)
        assert page.input_value(
            selectors_billing_address.ADDRESS1) == "Lvovskaya 1v", \
            "Street address 1 cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a street address 2")
@allure.story("Проверка ввода адреса 2")
def test_check_street_address_2(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод адреса 2"):
        street_address_2_field = page.query_selector(selectors_billing_address.ADDRESS2)
        street_address_2_field.fill("Rodionova 136")
        page.wait_for_timeout(2000)
        assert page.input_value(
            selectors_billing_address.ADDRESS2) == "Rodionova 136", \
            "Street address 2 cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a city")
@allure.story("Проверка ввода города")
def test_check_city(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод города"):
        city_field = page.query_selector(selectors_billing_address.CITY)
        city_field.fill("Nizhny Novgorod")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.CITY) == \
               "Nizhny Novgorod", "City cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a zip")
@allure.story("Проверка ввода индекса")
def test_check_postal_code(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод индекса"):
        postal_code_field = page.query_selector(selectors_billing_address.ZIP)
        postal_code_field.fill('603093')
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.ZIP) == "603093", \
            "Postal code cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a phone number")
@allure.story("Проверка ввода номера")
def test_check_phone(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод номера"):
        phone_field = page.query_selector(selectors_billing_address.PHONE)
        phone_field.fill("+7(831)436‒17‒52")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.PHONE) == \
               "+7(831)436‒17‒52", "Phone cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering an email")
@allure.story("Проверка ввода почтового адреса")
def test_check_email(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод почтового адреса"):
        email_field = page.query_selector(selectors_billing_address.EMAIL)
        email_field.fill('student@edu.hse.ru')
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_billing_address.EMAIL) == \
               'student@edu.hse.ru', "Email cannot be entered"
    with allure.step("Переход к оплате заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_2)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка обработки валидности почтового адреса"):
        assert (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                'student@edu.hse.ru') is None and page.locator("div").filter(
                has_text=re.compile(r"^The email must be valid$"))) or \
                (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                 'student@edu.hse.ru') is not None and
                page.locator("div").filter(has_text=re.compile(
                    r"^The email must be valid$") is None)), \
               "Wrong email handling"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of choosing a country")
@allure.story("Проверка выбора страны")
def test_check_country(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Выбор страны"):
        values = ['US', 'CA']
        for i in values:
            country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
            country_dropdown.select_option(value=i)
            page.wait_for_timeout(2000)
            assert country_dropdown.input_value() == i, "Country dropdown not working"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of choosing a province")
@allure.story("Проверка выбора провинций")
def test_check_province(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_products_page.PAGE_LINK)
        page.wait_for_timeout(2000)
    with allure.step("Добавление товаров в корзину"):
        products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
        products[3].click()
        page.wait_for_timeout(2000)
        close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
        close_button.click()
        page.wait_for_timeout(1000)
        cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
        cart_link.click()
        page.wait_for_timeout(2000)
    with allure.step("Переход к оформлению заказа"):
        next_step_button = page.query_selector(selectors_cart_page.NEXT_STEP_1)
        next_step_button.click()
        page.wait_for_timeout(2000)
    with allure.step("Выбор провинции (Канада)"):
        values_ca = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
        country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
        country_dropdown.select_option(value='CA')
        page.wait_for_timeout(2000)
        province_dropdown = page.query_selector(selectors_billing_address.PROVINCE)
        for i in values_ca:
            province_dropdown.select_option(value=i)
            page.wait_for_timeout(2000)
            assert province_dropdown.input_value() == i, "Province dropdown not working"
        with allure.step("Выбор провинции (США)"):
            values_us = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL',
                         'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH',
                         'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
                         'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC',
                         'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AA',
                         'AE', 'AP']
            country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
            country_dropdown.select_option(value='US')
            page.wait_for_timeout(2000)
            province_dropdown = page.query_selector(selectors_billing_address.PROVINCE)
            for i in values_us:
                province_dropdown.select_option(value=i)
                page.wait_for_timeout(2000)
                assert province_dropdown.input_value() == i, "Province dropdown not working"
