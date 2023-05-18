from project_selectors.locators import SelectorsBasePage, SelectorsCartPage
from project_selectors.locators import SelectorsProductsPage, SelectorsContactPage
from project_selectors.locators import SelectorsAboutPage, SelectorsMenuPage
import pytest
import allure
from Base import BasePage as bp

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@allure.feature("Navigation menu functionality checking")
class Tests:
    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Check the visibility of navigation menu")
    @allure.story("Проверка видимости каждой кнопки навигационного меню")
    def test_menu_is_visible(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Проверка видимости кнопки 'home'"):
            link = page.get(SelectorsBasePage.HOME_PAGE_LINK)
            assert link.inner_text().upper() == "HOME", \
                                                "Home button is invisible"
        with allure.step("Проверка видимости кнопки 'menu'"):
            link = page.get(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
            assert link.inner_text().upper() == "OUR MENU", \
                                                "Menu button is invisible"
        with allure.step("Проверка видимости кнопки 'products'"):
            link = page.get(SelectorsProductsPage.PRODUCTS_PAGE_LINK)
            assert link.inner_text().upper() == "PRODUCTS", \
                                                "Products button is invisible"
        with allure.step("Проверка видимости кнопки 'about'"):
            link = page.get(SelectorsAboutPage.ABOUT_PAGE_LINK)
            assert link.inner_text().upper() == "ABOUT", \
                                                "About button is invisible"
        with allure.step("Проверка видимости кнопки 'contact us'"):
            link = page.get(SelectorsContactPage.CONTACTUS_PAGE_LINK)
            assert link.inner_text().upper() == "CONTACT US", \
                                                "Contact button is invisible"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to home page throw navigation menu")
    @allure.story("Переход на домашнюю страницу с помощью навигационного меню")
    def test_go_to_home_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на домашнюю страницу"):
            page.click_button(SelectorsBasePage.HOME_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsBasePage.HOME_PAGE_TITLE)
            assert title.inner_text().upper() == "IMPRESSO ESPRESSO", \
                "Link to home page is not working"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to menu page throw navigation menu")
    @allure.story("Переход на страницу 'меню' с помощью навигационного меню")
    def test_go_to_our_menu_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на страницу 'меню'"):
            page.click_button(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsMenuPage.OUR_MENU_PAGE_TITLE)
            assert title.inner_text().upper() == "OUR MENU", \
                "Link to our menu page is not working"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to products page throw navigation menu")
    @allure.story("Переход на страницу 'продукты' с помощью навигационного меню")
    def test_go_to_products_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на страницу 'продукты'"):
            page.click_button(SelectorsProductsPage.PRODUCTS_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsProductsPage.PRODUCTS_PAGE_TITLE)
            assert title.inner_text().upper() == "PRODUCTS", \
                "Link to products page is not working"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to about page throw navigation menu")
    @allure.story("Переход на страницу 'о нас' с помощью навигационного меню")
    def test_go_to_about_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на страницу 'о нас'"):
            page.click_button(SelectorsAboutPage.ABOUT_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsAboutPage.ABOUT_PAGE_TITLE)
            assert title.inner_text().upper() == "ABOUT US", \
                "Link to about page is not working"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to contact us page throw navigation menu")
    @allure.story("Переход на страницу 'контакты' с помощью навигационного меню")
    def test_go_to_contactus_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на страницу 'контакты'"):
            page.click_button(SelectorsContactPage.CONTACTUS_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsContactPage.CONTACTUS_PAGE_TITLE)
            assert title.inner_text().upper() == "CONTACT US", \
                "Link to contact us page is not working"

    @pytest.mark.parametrize('setup_browser', browsers)
    @pytest.mark.fast
    @allure.feature("Move to cart page throw navigation menu")
    @allure.story("Переход на страницу 'корзина' с помощью навигационного меню")
    def test_go_to_cart_page(self, setup_browser, request):
        with allure.step("Запуск браузера и открытие страницы"):
            newpage = request.getfixturevalue(setup_browser)
            page = bp(newpage)
        with allure.step("Переход на страницу 'корзина'"):
            page.click_button(SelectorsCartPage.CART_PAGE_LINK)
        with allure.step("Проверка правильности перехода"):
            title = page.get(
                SelectorsCartPage.CART_PAGE_TITLE)
            assert title.inner_text().upper() == "MY CART", \
                "Link to cart page is not working"
