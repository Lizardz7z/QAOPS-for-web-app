from project_selectors.locators import SelectorsBasePage
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
        link = page.query_selector(SelectorsBasePage.HOME_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Проверка правильности перехода"):
        title = page.query_selector(
            SelectorsBasePage.HOME_PAGE_TITLE)
        assert title.inner_text().upper() == "IMPRESSO ESPRESSO", \
            "Home page is not opened"
    with allure.step("Проверка видимости 'our community'"):
        link = page.query_selector(SelectorsBasePage.COMMUNITY_TITLE)
        assert link.inner_text() == "~ Our Community ~", \
            "Community title is invisible"
    with allure.step("Проверка видимости customer comments part"):
        link = page.query_selector(SelectorsBasePage.CUSTOMER_TITLE)
        assert link.inner_text() == "~ Our Customer Testimonials ~", \
            "Customer title is invisible"
    with allure.step("Проверка видимости панели выбора вида кофе"):
        link = page.query_selector(SelectorsBasePage.COFFEE_TITLE)
        assert link.inner_text() == "Choose Your Style // Choose Your Flavor", \
            "Coffee choosing title is invisible"