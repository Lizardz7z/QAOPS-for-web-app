import pytest
import allure

from Contact_us import ContactUsPage

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering a name")
@allure.story("Проверка ввода имени")
def test_check_name_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        contact_us = ContactUsPage(page)
        contact_us.contact_us_link()
    with allure.step("Ввод имени"):
        name_field = contact_us.get_name()
        name_field.fill("Lisa and Masha")
        contact_us.wait()
        assert contact_us.name_value() == "Lisa and Masha", \
            "Name cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering an email")
@allure.story("Проверка ввода почтового адреса")
def test_check_email_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        contact_us = ContactUsPage(page)
        contact_us.contact_us_link()
    with allure.step("Ввод почтового адреса"):
        name_field = contact_us.get_email()
        name_field.fill("student@edu.hse.ru")
        contact_us.wait()
        assert contact_us.email_value() == "student@edu.hse.ru", \
            "Email cannot be entered"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.slow
@allure.feature("Contact us functionality checking")
@allure.feature("Сhecking the possibility of entering an description")
@allure.story("Проверка ввода сообщения")
def test_check_description_contact_us(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        contact_us = ContactUsPage(page)
        contact_us.contact_us_link()
    with allure.step("Ввод сообщения"):
        name_field = contact_us.get_description()
        name_field.fill("We love coffee!")
        contact_us.wait()
        assert contact_us.description_value() == "We love coffee!", \
            "Description cannot be entered"