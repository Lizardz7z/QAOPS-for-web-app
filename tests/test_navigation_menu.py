from selectrs.locators import *
import pytest
import allure

@allure.feature("Navigation menu functionality checking")
class Tests:
    @pytest.mark.fast
    @allure.feature("Move to home page throw navigation menu")
    @allure.story("Переход на домашнюю страницу с помощью навигационного меню")
    def test_go_to_home_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на домашнюю страницу"):
            link = page.query_selector(selectors_base_page.HOME_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_base_page.HOME_PAGE_TITLE)
            assert title.inner_text().upper() == "IMPRESSO ESPRESSO", "Link to home page is not working"

    @pytest.mark.fast
    @allure.feature("Move to menu page throw navigation menu")
    @allure.story("Переход на страницу 'меню' с помощью навигационного меню")
    def test_go_to_our_menu_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на страницу 'меню'"):
            link = page.query_selector(selectors_menu_page.OUR_MENU_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_menu_page.OUR_MENU_PAGE_TITLE)
            assert title.inner_text().upper() == "OUR MENU", "Link to our menu page is not working"

    @pytest.mark.fast
    @allure.feature("Move to products page throw navigation menu")
    @allure.story("Переход на страницу 'продукты' с помощью навигационного меню")
    def test_go_to_products_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на страницу 'продукты'"):
            link = page.query_selector(selectors_products_page.PRODUCTS_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_products_page.PRODUCTS_PAGE_TITLE)
            assert title.inner_text().upper() == "PRODUCTS", "Link to products page is not working"

    @pytest.mark.fast
    @allure.feature("Move to about page throw navigation menu")
    @allure.story("Переход на страницу 'о нас' с помощью навигационного меню")
    def test_go_to_about_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на страницу 'о нас'"):
            link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_about_page.ABOUT_PAGE_TITLE)
            assert title.inner_text().upper() == "ABOUT US", "Link to about page is not working"

    @pytest.mark.fast
    @allure.feature("Move to contact us page throw navigation menu")
    @allure.story("Переход на страницу 'контакты' с помощью навигационного меню")
    def test_go_to_contactus_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на страницу 'контакты'"):
            link = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_contact_page.CONTACTUS_PAGE_TITLE)
            assert title.inner_text().upper() == "CONTACT US", "Link to contact us page is not working"

    @pytest.mark.fast
    @allure.feature("Move to cart page throw navigation menu")
    @allure.story("Переход на страницу 'корзина' с помощью навигационного меню")
    def test_go_to_cart_page(self, setup_browser):
        with allure.step("Запуск браузера и открытие страницы"):
            page = setup_browser
        with allure.step("Переход на страницу 'корзина'"):
            link = page.query_selector(selectors_cart_page.CART_PAGE_LINK)
            link.click()
            page.wait_for_timeout(2000)
        with allure.step("Проверка правильности перехода"):
            title = page.query_selector(selectors_cart_page.CART_PAGE_TITLE)
            assert title.inner_text().upper() == "MY CART", "Link to cart page is not working"

