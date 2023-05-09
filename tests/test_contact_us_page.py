import pytest
import allure

from selectrs.locators import selectors_contact_page

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering a name")
@allure.story("Проверка ввода имени")
def test_check_name_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_contact_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод имени"):
        name_field = page.query_selector(selectors_contact_page.NAME)
        name_field.fill("Lisa and Masha")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_contact_page.NAME) == "Lisa and Masha", \
            "Name cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering an email")
@allure.story("Проверка ввода почтового адреса")
def test_check_email_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_contact_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод почтового адреса"):
        name_field = page.query_selector(selectors_contact_page.EMAIL)
        name_field.fill("student@edu.hse.ru")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_contact_page.EMAIL) == "student@edu.hse.ru", \
            "Email cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering an description")
@allure.story("Проверка ввода сообщения")
def test_check_description_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_contact_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Ввод сообщения"):
        name_field = page.query_selector(selectors_contact_page.DESCRIPTION)
        name_field.fill("We love coffee!")
        page.wait_for_timeout(2000)
        assert page.input_value(selectors_contact_page.DESCRIPTION) == \
               "We love coffee!", \
            "Description cannot be entered"