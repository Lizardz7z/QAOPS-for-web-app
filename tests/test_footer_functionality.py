from selectrs.locators import selectors_base_page
from selectrs.locators import selectors_footer
from selectrs.locators import selectors_products_page
from selectrs.locators import selectors_about_page
from selectrs.locators import selectors_menu_page
from selectrs.locators import selectors_contact_page
import pytest
import allure

browsers = ['setup_browser_chrome', 'setup_browser_firefox']
testdata = [
    selectors_base_page.PAGE_LINK,
    selectors_menu_page.PAGE_LINK,
    selectors_products_page.PAGE_LINK,
    selectors_about_page.PAGE_LINK,
    selectors_contact_page.PAGE_LINK
]
@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking footer titles visibility")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_visibility(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
    with allure.step("Переход на страницу"):
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости 'Contacts'"):
        link = page.query_selector(selectors_footer.CONTACT_TITLE)
        assert link.inner_text() == "Contact Us", \
            "Contact title in footer is invisible"
    with allure.step("Проверка видимости 'Opening hours'"):
        link = page.query_selector(selectors_footer.OPEN_HOURS)
        assert link.inner_text() == "Opening Hours", \
            "Opening hours title is invisible"
    with allure.step("Проверка видимости панели выбора вида кофе"):
        link = page.query_selector(selectors_footer.SITE_LINKS)
        assert link.inner_text() == "Site Links", \
            "Site links title is invisible"


@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking link from footer to home page")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_link_to_home(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости ссылки"):
        link = page.query_selector(selectors_footer.HOME)
        assert link.inner_text() == "Home", \
            "Link to home page from footer is invisible"
    with allure.step("Переход на домашнюю страницу"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            selectors_base_page.HOME_PAGE_TITLE)
        assert title.inner_text().upper() == "IMPRESSO ESPRESSO", \
            "Link to home page from footer is not working"

@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking link from footer to menu page")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_link_to_menu(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости ссылки"):
        link = page.query_selector(selectors_footer.MENU)
        assert link.inner_text() == "Coffees, Drinks & Food Menu", \
            "Link to menu page from footer is invisible"
    with allure.step("Переход на страницу меню"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            selectors_menu_page.OUR_MENU_PAGE_TITLE)
        assert title.inner_text().upper() == "OUR MENU", \
            "Link to menu page from footer is not working"

@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking link from footer to products page")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_link_to_products(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости ссылки"):
        link = page.query_selector(selectors_footer.PRODUCTS)
        assert link.inner_text() == "Retail Products", \
            "Link to products page from footer is invisible"
    with allure.step("Переход на страницу товаров"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            selectors_products_page.PRODUCTS_PAGE_TITLE)
        assert title.inner_text().upper() == "PRODUCTS", \
            "Link to products page from footer is not working"

@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking link from footer to info page")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_link_to_info(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости ссылки"):
        link = page.query_selector(selectors_footer.ABOUT)
        assert link.inner_text() == "Impresso Espresso - About Us", \
            "Link to about page from footer is invisible"
    with allure.step("Переход на страницу о нас"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            selectors_about_page.ABOUT_PAGE_TITLE)
        assert title.inner_text().upper() == "ABOUT US", \
            "Link to about page from footer is not working"

@pytest.mark.parametrize("link_to", testdata)
@pytest.mark.parametrize("setup_browser", browsers)
@allure.feature("Checking link from footer to contact page")
@allure.story("Проверка отображения заголовков нижнего меню")
def test_footer_link_to_contacts(setup_browser, link_to, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(link_to)
        page.wait_for_timeout(2000)
    with allure.step("Проверка видимости ссылки"):
        link = page.query_selector(selectors_footer.CONTACT_LINK)
        assert link.inner_text() == "Contact Us", \
            "Link to contact page from footer is invisible"
    with allure.step("Переход на страницу контакты"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            selectors_contact_page.CONTACTUS_PAGE_TITLE)
        assert title.inner_text().upper() == "CONTACT US", \
            "Link to contact page from footer is not working"