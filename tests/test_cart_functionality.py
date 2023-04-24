from selectrs.locators import *
import re


def test_add_to_cart(setup_browser, close_browser):
    page, browser = setup_browser()
    #вставить переход на страницу "продукты" (этот тест должен выполняться при условии прохождение тестов на открытие корзины и страницы "продукты"
    products = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
    close_button = page.query_selector(selectors_cart_page.CART_CLOSE_BUTTON)
    our_products = {products[i].get_attribute(selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper(): 0
                    for i in range(len(products))}
    for i in range(len(products)):
        products[i].click()
        our_products[products[i].get_attribute(selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
        page.wait_for_timeout(2000)
        close_button.click()
        page.wait_for_timeout(1000)
    products[3].click()
    our_products[products[3].get_attribute(selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper()] += 1
    cart_link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
    cart_link.click()
    page.wait_for_timeout(2000)
    products_in_cart = page.query_selector_all(selectors_cart_page.ITEMS_IN_CART)
    products_names_in_cart = {}
    for i in range(len(products_in_cart)):
        products_names_in_cart[products_in_cart[i].query_selector(selectors_cart_page.PRODUCT_NAME).inner_text()] = \
            int(products_in_cart[i].query_selector(selectors_cart_page.QUANTITY).inner_text())
    for i in our_products.items():
        assert products_names_in_cart[i[0]] == i[1], "Products added to cart incorrectly"
    close_browser(browser)


def test_check_prices(setup_browser, close_browser):
    page, browser = setup_browser()
    # заставить этот тест выполняться только при условии, что выполнен предыдущий (добавление в корзину)
    prices = page.query_selector_all(selectors_cart_page.ITEMS_IN_CART)
    prices_home = page.query_selector_all(selectors_products_page.ITEMS_SELECTOR)
    page.wait_for_timeout(2000)
    our_products = {prices_home[i].get_attribute(selectors_cart_page.DATA_ITEM_NAME_ATTRIBUTE).upper():
                    float(prices_home[i].get_attribute(selectors_cart_page.DATA_ITEM_PRICE_ATTRIBUTE))
                    for i in range(len(prices_home))}
    subtotal = 0.0
    for i in range(len(prices)):
        total = prices[i].query_selector(selectors_cart_page.UNIT_PRICE)
        total = float(total.inner_text()[1:])
        assert total == our_products[prices[i].query_selector(selectors_cart_page.PRODUCT_NAME).inner_text()], \
            "The price calculated incorrectly"
        total *= int(prices[i].query_selector(selectors_cart_page.QUANTITY).inner_text())
        total_price = prices[i].query_selector(selectors_cart_page.TOTAL_PRICE).inner_text()[1:]
        assert total == float(total_price), "The total price calculated incorrectly"
        subtotal += float(total)
    sum_of_products = page.query_selector(selectors_cart_page.SUM_OF_PRODUCTS)
    s1 = sum_of_products.inner_text()
    s1 = float(s1[1:])
    assert s1 == subtotal, "The subtotal price calculated incorrectly"
    close_browser(browser)


def test_next_step(page, selector):
    next_step_button = page.query_selector(selector)
    next_step_button.click()
    page.wait_for_timeout(2000)


def test_check_empty_fields(page):
    test_next_step(page, selectors_cart_page.NEXT_STEP_2)
    assert page.locator("div").filter(has_text=re.compile(r"^NameThis field is required$")), "No empty name handling"
    assert page.locator("div").filter(has_text=re.compile(r"^StreetAddressThis field is required$")), \
        "No empty street address handling"
    assert page.locator("div").filter(has_text=re.compile(r"^CityThis field is required$")), "No empty city handling"
    assert page.locator("div").filter(has_text=re.compile(r"^ZIP / Postal codeThis field is required$")), \
        "No empty zip handling"
    assert page.locator("div").filter(has_text=re.compile(r"^EmailThis field is required$")), "No empty email handling"


def test_check_name(page, name):
    name_field = page.query_selector(selectors_billing_address.NAME)
    name_field.fill(name)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.NAME) == name, "Name cannot be entered"


def test_check_company_name(page, company_name):
    company_name_field = page.query_selector(selectors_billing_address.COMPANY)
    company_name_field.fill(company_name)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.COMPANY) == company_name, "Name cannot be entered"


def test_check_street_address(page, street_address):
    street_address_field = page.query_selector(selectors_billing_address.ADDRESS1)
    street_address_field.fill(street_address)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.ADDRESS1) == street_address, "Street address 1 cannot be entered"


def test_check_street_address_2(page, street_address_2):
    street_address_2_field = page.query_selector(selectors_billing_address.ADDRESS2)
    street_address_2_field.fill(street_address_2)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.ADDRESS2) == street_address_2, "Street address 2 cannot be entered"


def test_check_city(page, city):
    city_field = page.query_selector(selectors_billing_address.CITY)
    city_field.fill(city)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.CITY) == city, "City cannot be entered"


def test_check_postal_code(page, postal_code):
    postal_code_field = page.query_selector(selectors_billing_address.ZIP)
    postal_code_field.fill(postal_code)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.ZIP) == postal_code, "Postal code cannot be entered"


def test_check_phone(page, phone):
    phone_field = page.query_selector(selectors_billing_address.PHONE)
    phone_field.fill(phone)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.PHONE) == phone, "Phone cannot be entered"


def test_check_email(page, email):
    email_field = page.query_selector(selectors_billing_address.EMAIL)
    email_field.fill(email)
    page.wait_for_timeout(2000)
    assert page.input_value(selectors_billing_address.EMAIL) == email, "Email cannot be entered"
    test_next_step(page, selectors_cart_page.NEXT_STEP_2)
    assert (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is None and
            page.locator("div").filter(has_text=re.compile(r"^The email must be valid$"))) or \
           (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is not None and
            page.locator("div").filter(has_text=re.compile(r"^The email must be valid$") is None)), "Wrong email " \
                                                                                                    "handling "


def test_check_country(page):
    values = ['US', 'CA']
    for i in values:
        country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
        country_dropdown.select_option(value=i)
        page.wait_for_timeout(2000)
        assert country_dropdown.input_value() == i, "Country dropdown not working"


def test_check_province(page):
    values_ca = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    values_us = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL',
                 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
                 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX',
                 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AA', 'AE', 'AP']
    country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
    country_dropdown.select_option(value='US')
    page.wait_for_timeout(2000)
    province_dropdown = page.query_selector(selectors_billing_address.PROVINCE)
    for i in values_us:
        province_dropdown.select_option(value=i)
        page.wait_for_timeout(2000)
        assert province_dropdown.input_value() == i, "Province dropdown not working"
    country_dropdown = page.query_selector(selectors_billing_address.COUNTRY)
    country_dropdown.select_option(value='CA')
    page.wait_for_timeout(2000)
    province_dropdown = page.query_selector(selectors_billing_address.PROVINCE)
    for i in values_ca:
        province_dropdown.select_option(value=i)
        page.wait_for_timeout(2000)
        assert province_dropdown.input_value() == i, "Province dropdown not working"
