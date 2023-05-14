import pytest
import allure

from Our_menu import MenuPage

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'all' is clickable")
@allure.story("Проверка кнопки all")
def test_check_all_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку all"):
        all_button = menu.button("all")
        all_button.click()
        titles = menu.dishes()
        products = ["Island Pitaya", "Vanilla Blue Sky", "Tomato Soup",
                    "Broccoli & Cheddar Soup", "Ham, Egg & Cheese",
                    "Egg & Cheese", "Avocad Egg White", 'Bacon Egg & Cheese',
                    "Greek Salad", "Caesar Salad", "Chicken Burrito",
                    "Breakfast Burrito", "Red Velvet",
                    "Blueberry Restorer", "Island Tropics",
                    "Healthy Glow", "Cinnamon Roll", "Iced Lemon Cake",
                    "Classic Coffee Cake", "Cream Cheese Danish",
                    "Blueberry Muffin", "Double Chocolate Chip Muffin",
                    "Chocolate Croissant", "Almond Croissant", "Croissant",
                    "Chocolate Cake Pop", "Dozen Bagels"
                    "Half Dozen Bagel Box", "Poppy Seed Bagel", "Sesame Bagel",
                    "Potato Roll", "Honey Whole Wheat"
                    "Cinnamon Raisin Bagel", "Blueberry Bagel",
                    "Spinach Bagel", "Cinnamon Sugar Bagel", "Plain Bagel"
                    "Everything Bagel", "Cold Brew Coffee",
                    "Pumpkin Cream Cold Brew", "Peppermint Mocha",
                    "Salted Caramel Mocha", "Frappè",
                    "Ras Chai", "Earl Grey (Organic)", "Rooibos Bergamot",
                    "Moroccan Mint", "Cappuccino", "Flat White",
                    "Latte Macchiato", "Caffè Latte", "Mocha",
                    "Doppio", "Caffè Americano"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'all' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'acai bowls' is clickable")
@allure.story("Проверка кнопки acai bowls")
def test_check_acai_bowls_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку acai bowls"):
        acai_bowls_button = menu.button('Acai Bowls')
        acai_bowls_button.click()
        titles = menu.dishes()
        products = ["Island Pitaya", "Vanilla Blue Sky"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'acai bowls' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'soups' is clickable")
@allure.story("Проверка кнопки soups")
def test_check_soups_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку soups"):
        soups_button = menu.button('soups')
        soups_button.click()
        titles = menu.dishes()
        products = ["Tomato Soup", "Broccoli & Cheddar Soup"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'soups' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'breakfast sandwiches' is clickable")
@allure.story("Проверка кнопки breakfast sandwiches")
def test_check_breakfast_sandwiches_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку breakfast sandwiches"):
        breakfast_sandwiches_button = menu.button('breakfast sandwiches')
        breakfast_sandwiches_button.click()
        titles = menu.dishes()
        products = ["Ham, Egg & Cheese", "Egg & Cheese",
                    "Avocad Egg White", 'Bacon Egg & Cheese']
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'breakfast sandwiches' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'salads' is clickable")
@allure.story("Проверка кнопки salads")
def test_check_salads_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку salads"):
        salads_button = menu.button('salads')
        salads_button.click()
        titles = menu.dishes()
        products = ["Greek Salad", "Caesar Salad"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'salads' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'burritos' is clickable")
@allure.story("Проверка кнопки burritos")
def test_check_burritos_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку burritos"):
        burritos_button = menu.button('Burritos')
        burritos_button.click()
        titles = menu.dishes()
        products = ["Chicken Burrito", "Breakfast Burrito"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'burritos' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'smoothies' is clickable")
@allure.story("Проверка кнопки smoothies")
def test_check_smoothies_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку smoothies"):
        smoothies_button = menu.button('smoothies')
        smoothies_button.click()
        titles = menu.dishes()
        products = ["Red Velvet", "Blueberry Restorer",
                    "Island Tropics", "Healthy Glow"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'smoothies' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'bakery' is clickable")
@allure.story("Проверка кнопки bakery")
def test_check_bakery_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку bakery"):
        bakery_button = menu.button('bakery')
        bakery_button.click()
        titles = menu.dishes()
        products = ["Cinnamon Roll", "Iced Lemon Cake",
                    "Classic Coffee Cake", "Cream Cheese Danish",
                    "Blueberry Muffin", "Double Chocolate Chip Muffin",
                    "Chocolate Croissant", "Almond Croissant",
                    "Croissant", "Chocolate Cake Pop"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'bakery' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'bagels' is clickable")
@allure.story("Проверка кнопки bagels")
def test_check_bagels_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку bagels"):
        bagels_button = menu.button('bagels')
        bagels_button.click()
        titles = menu.dishes()
        products = ["Dozen Bagels", "Half Dozen Bagel Box",
                    "Poppy Seed Bagel", "Sesame Bagel",
                    "Potato Roll", "Honey Whole Wheat",
                    "Cinnamon Raisin Bagel", "Blueberry Bagel",
                    "Spinach Bagel", "Cinnamon Sugar Bagel",
                    "Plain Bagel", "Everything Bagel"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'bagels' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'coffee' is clickable")
@allure.story("Проверка кнопки coffee")
def test_check_coffee_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку coffee"):
        coffee_button = menu.button('coffee')
        coffee_button.click()
        titles = menu.dishes()
        products = ["Cold Brew Coffee", "Pumpkin Cream Cold Brew",
                    "Peppermint Mocha", "Salted Caramel Mocha",
                    "Frappè", "Cappuccino", "Flat White",
                    "Latte Macchiato", "Caffè Latte", "Mocha",
                    "Doppio", "Caffè Americano"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'coffee' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'tea' is clickable")
@allure.story("Проверка кнопки tea")
def test_check_tea_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        menu = MenuPage(page)
        menu.menu_link()
    with allure.step("Нажатие на кнопку tea"):
        tea_button = menu.button('tea')
        tea_button.click()
        titles = menu.dishes()
        products = ["Ras Chai", "Earl Grey (Organic)", "Rooibos Bergamot",
                    "Moroccan Mint"]
        for i in range(len(titles)):
            assert titles[i].inner_text() == products[i], \
                "The button 'tea' is not clickable"
