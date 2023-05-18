import Home as h
import pytest
import allure

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Checking titles visibility")
@allure.story("Проверка отображения заголовков отделов главной страницы")
def test_titles_visibility(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
    with allure.step("Переход на домашнюю страницу"):
        hp=h.HomePage(page)
        hp.home_link()
    with allure.step("Проверка правильности перехода"):
        title = hp.get(h.Home.HOME_PAGE_TITLE)
        assert title.inner_text().upper() == "IMPRESSO ESPRESSO", \
            "Home page is not opened"
    with allure.step("Проверка видимости 'our community'"):
        title = hp.get(h.Home.COMMUNITY_TITLE)
        assert title.inner_text() == "~ Our Community ~", \
            "Community title is invisible"
    with allure.step("Проверка видимости customer comments part"):
        title = hp.get(h.Home.CUSTOMER_TITLE)
        assert title.inner_text() == "~ Our Customer Testimonials ~", \
            "Customer title is invisible"
    with allure.step("Проверка видимости панели выбора вида кофе"):
        title = hp.get(h.Home.COFFEE_TITLE)
        assert title.inner_text() == "Choose Your Style // Choose Your Flavor", \
            "Coffee choosing title is invisible"
