import re
from Products import Products
from Cart import Cart
from Billing_address import BillingAddress
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
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        our_products = product.our_products()
        for i in range(len(products)):
            products[i].click()
            our_products[product.product(products[i])] += 1
            product.wait()
            product.close_button()
        products[3].click()
        our_products[product.product(products[3])] += 1
        cart = Cart(product.page)
        cart.cart_page()
        products_in_cart = cart.products_in_cart()
        products_names_in_cart = {}
    with allure.step("Проверка правильности добавления товаров"):
        for i in range(len(products_in_cart)):
            products_names_in_cart[cart.product_name(products_in_cart[i])] = \
                int(cart.quantity(products_in_cart[i]))
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
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        our_products = product.our_products()
        for i in range(len(products)):
            products[i].click()
            our_products[product.product(products[i])] += 1
            product.wait()
            product.close_button()
        products[3].click()
        our_products[product.product(products[3])] += 1
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Проверка подсчитанной стоимости"):
        prices = cart.products_in_cart()
        product.wait()
        our_products = product.our_products_prices()
        subtotal = 0.0
        for i in range(len(prices)):
            total = cart.unit_price(prices[i])
            total = float(total.inner_text()[1:])
            assert total == our_products[cart.product_name(prices[i])], \
                "The price calculated incorrectly"
            total *= int(cart.quantity(prices[i]))
            total_price = cart.total_price(prices[i])[1:]
            assert total == float(total_price), "The total price calculated incorrectly"
            subtotal += float(total)
        sum_of_products = cart.sum()
        s1 = sum_of_products.inner_text()
        s1 = float(s1[1:])
        assert s1 == subtotal, "The subtotal price calculated incorrectly"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the removal of an item from the cart")
@allure.story("Проверка удаления товара из корзины")
def test_removing_an_item_from_the_cart(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Удаление товара из корзины"):
        delete_button = cart.delete_button()
        delete_button.click()
        product.wait()
        assert cart.empty_cart_message() == "THE CART IS NOW EMPTY. SELECT " \
               "SOME PRODUCTS TO BUY BEFORE CHECKING OUT.", \
               "Items are not deleted"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сheck a privacy display")
@allure.story("Проверка наличия надписи о шифровании данных при оплате")
def test_privacy_display(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Проверка наличия надписи о шифровании"):
        protect = cart.protect()
        assert protect == "POWERED AND SECURED BY SNIPCART", \
            "Encryption information is not displayed"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the ability to go to the next page")
@allure.story("Проверка перехода на страницу вперед")
def test_next_step(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        product.wait()


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the ability to go to the previous page")
@allure.story("Проверка перехода на предыдущую страницу")
def test_previous_step(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        product.wait()
    with allure.step("Переход на страницу назад"):
        next_step_button = cart.previous_step()
        next_step_button.click()
        product.wait()


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking for empty fields")
@allure.story("Проверка пустых полей")
def test_check_empty_fields(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        product.wait()
    with allure.step("Проверка пустого имени"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^NameThis field is required$")), \
            "No empty name handling"
    with allure.step("Проверка пустого адреса"):
        assert page.locator("div").filter(has_text=re.compile(
            r"^StreetAddressThis field is required$")), \
            "No empty street address handling"
    with allure.step("Проверка пустого города"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^CityThis field is required$")), \
            "No empty city handling"
    with allure.step("Проверка пустого индекса"):
        assert page.locator("div").filter(has_text=re.compile(
            r"^ZIP / Postal codeThis field is required$")), \
            "No empty zip handling"
    with allure.step("Проверка пустого почтового адреса"):
        assert page.locator("div").filter(
            has_text=re.compile(r"^EmailThis field is required$")), \
            "No empty email handling"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a name")
@allure.story("Проверка ввода имени")
def test_check_name(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод имени"):
        b_a = BillingAddress(cart.page)
        name_field = b_a.name()
        name_field.fill("Lisa and Masha")
        b_a.wait()
        assert b_a.name_value() == "Lisa and Masha", \
            "Name cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a company name")
@allure.story("Проверка ввода названия компании")
def test_check_company_name(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод названия компании"):
        b_a = BillingAddress(cart.page)
        company_name_field = b_a.company()
        company_name_field.fill("HSE")
        b_a.wait()
        assert b_a.company_value() == 'HSE', "Company cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a street address")
@allure.story("Проверка ввода адреса 1")
def test_check_street_address(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод адреса 1"):
        b_a = BillingAddress(cart.page)
        street_address_field = b_a.address()
        street_address_field.fill("Lvovskaya 1v")
        b_a.wait()
        assert b_a.address_value() == "Lvovskaya 1v", \
            "Street address 1 cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a street address 2")
@allure.story("Проверка ввода адреса 2")
def test_check_street_address_2(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод адреса 2"):
        b_a = BillingAddress(cart.page)
        street_address_2_field = b_a.address2()
        street_address_2_field.fill("Rodionova 136")
        b_a.wait()
        assert b_a.address2_value() == "Rodionova 136", \
            "Street address 2 cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a city")
@allure.story("Проверка ввода города")
def test_check_city(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод города"):
        b_a = BillingAddress(cart.page)
        city_field = b_a.city()
        city_field.fill("Nizhny Novgorod")
        b_a.wait()
        assert b_a.city_value() == "Nizhny Novgorod", \
            "City cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a zip")
@allure.story("Проверка ввода индекса")
def test_check_postal_code(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод индекса"):
        b_a = BillingAddress(cart.page)
        postal_code_field = b_a.zip()
        postal_code_field.fill('603093')
        b_a.wait()
        assert b_a.zip_value() == "603093", \
            "Postal code cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering a phone number")
@allure.story("Проверка ввода номера")
def test_check_phone(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод номера"):
        b_a = BillingAddress(cart.page)
        phone_field = b_a.phone()
        phone_field.fill('+7(831)436‒17‒52')
        b_a.wait()
        assert b_a.phone_value() == "+7(831)436‒17‒52", \
            "Phone cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of entering an email")
@allure.story("Проверка ввода почтового адреса")
def test_check_email(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Ввод почтового адреса"):
        b_a = BillingAddress(cart.page)
        email_field = b_a.email()
        email_field.fill('student@edu.hse.ru')
        b_a.wait()
        assert b_a.email_value() == \
               'student@edu.hse.ru', "Email cannot be entered"
    with allure.step("Переход к оплате заказа"):
        next_step_button = b_a.next_step_2()
        next_step_button.click()
        b_a.wait()
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
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Выбор страны"):
        b_a = BillingAddress(cart.page)
        values = ['US', 'CA']
        for i in values:
            country_dropdown = b_a.country()
            country_dropdown.select_option(value=i)
            b_a.wait()
            assert country_dropdown.input_value() == i, "Country dropdown not working"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Cart functionality checking")
@allure.feature("Сhecking the possibility of choosing a province")
@allure.story("Проверка выбора провинций")
def test_check_province(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        product = Products(page)
        product.products_page()
    with allure.step("Добавление товаров в корзину"):
        products = product.products()
        products[3].click()
        product.wait()
        product.close_button()
        cart = Cart(product.page)
        cart.cart_page()
    with allure.step("Переход к оформлению заказа"):
        next_step_button = cart.next_step_1()
        next_step_button.click()
        cart.wait()
    with allure.step("Выбор провинции (Канада)"):
        b_a = BillingAddress(cart.page)
        values_ca = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON',
                     'PE', 'QC', 'SK', 'YT']
        country_dropdown = b_a.country()
        country_dropdown.select_option(value='CA')
        b_a.wait()
        province_dropdown = b_a.province()
        for i in values_ca:
            province_dropdown.select_option(value=i)
            b_a.wait()
            assert province_dropdown.input_value() == i, "Province dropdown not working"
        with allure.step("Выбор провинции (США)"):
            values_us = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
                         'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                         'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO',
                         'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP',
                         'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN',
                         'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AA',
                         'AE', 'AP']
            country_dropdown = b_a.country()
            country_dropdown.select_option(value='US')
            b_a.wait()
            province_dropdown = b_a.province()
            for i in values_us:
                province_dropdown.select_option(value=i)
                b_a.wait()
                assert province_dropdown.input_value() == i, \
                    "Province dropdown not working"
