from project_selectors.locators import SelectorsBasePage
from project_selectors.locators import SelectorsFooter
from project_selectors.locators import SelectorsProductsPage
from project_selectors.locators import SelectorsAboutPage
from project_selectors.locators import SelectorsMenuPage
from project_selectors.locators import SelectorsContactPage
import pytest
import allure

browsers = ['setup_browser_chrome', 'setup_browser_firefox']
testdata = [
    SelectorsBasePage.PAGE_LINK,
    SelectorsMenuPage.PAGE_LINK,
    SelectorsProductsPage.PAGE_LINK,
    SelectorsAboutPage.PAGE_LINK,
    SelectorsContactPage.PAGE_LINK
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
        link = page.query_selector(SelectorsFooter.CONTACT_TITLE)
        assert link.inner_text() == "Contact Us", \
            "Contact title in footer is invisible"
    with allure.step("Проверка видимости 'Opening hours'"):
        link = page.query_selector(SelectorsFooter.OPEN_HOURS)
        assert link.inner_text() == "Opening Hours", \
            "Opening hours title is invisible"
    with allure.step("Проверка видимости панели выбора вида кофе"):
        link = page.query_selector(SelectorsFooter.SITE_LINKS)
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
        link = page.query_selector(SelectorsFooter.HOME)
        assert link.inner_text() == "Home", \
            "Link to home page from footer is invisible"
    with allure.step("Переход на домашнюю страницу"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsBasePage.HOME_PAGE_TITLE)
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
        link = page.query_selector(SelectorsFooter.MENU)
        assert link.inner_text() == "Coffees, Drinks & Food Menu", \
            "Link to menu page from footer is invisible"
    with allure.step("Переход на страницу меню"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsMenuPage.OUR_MENU_PAGE_TITLE)
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
        link = page.query_selector(SelectorsFooter.PRODUCTS)
        assert link.inner_text() == "Retail Products", \
            "Link to products page from footer is invisible"
    with allure.step("Переход на страницу товаров"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsProductsPage.PRODUCTS_PAGE_TITLE)
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
        link = page.query_selector(SelectorsFooter.ABOUT)
        assert link.inner_text() == "Impresso Espresso - About Us", \
            "Link to about page from footer is invisible"
    with allure.step("Переход на страницу о нас"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsAboutPage.ABOUT_PAGE_TITLE)
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
        link = page.query_selector(SelectorsFooter.CONTACT_LINK)
        assert link.inner_text() == "Contact Us", \
            "Link to contact page from footer is invisible"
    with allure.step("Переход на страницу контакты"):
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsContactPage.CONTACTUS_PAGE_TITLE)
        assert title.inner_text().upper() == "CONTACT US", \
            "Link to contact page from footer is not working"
