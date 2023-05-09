import pytest
import allure

from project_selectors.locators import SelectorsMenuPage

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'all' is clickable")
@allure.story("Проверка кнопки all")
def test_check_all_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку all"):
        all_button = page.get_by_role("button", name='all')
        all_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
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
            assert titles[1].inner_text() == products[i], \
                "The button 'all' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'acai bowls' is clickable")
@allure.story("Проверка кнопки acai bowls")
def test_check_acai_bowls_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку acai bowls"):
        acai_bowls_button = page.get_by_role("button", name='Acai Bowls')
        acai_bowls_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Island Pitaya", "Vanilla Blue Sky"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'acai bowls' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'soups' is clickable")
@allure.story("Проверка кнопки soups")
def test_check_soups_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку soups"):
        soups_button = page.get_by_role("button", name='soups')
        soups_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Tomato Soup", "Broccoli & Cheddar Soup"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'soups' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'breakfast sandwiches' is clickable")
@allure.story("Проверка кнопки breakfast sandwiches")
def test_check_breakfast_sandwiches_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку breakfast sandwiches"):
        breakfast_sandwiches_button = page.get_by_role("button",
                                                       name='breakfast sandwiches')
        breakfast_sandwiches_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Ham, Egg & Cheese", "Egg & Cheese",
                    "Avocad Egg White", 'Bacon Egg & Cheese']
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'breakfast sandwiches' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'salads' is clickable")
@allure.story("Проверка кнопки salads")
def test_check_salads_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку salads"):
        salads_button = page.get_by_role("button", name='salads')
        salads_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Greek Salad", "Caesar Salad"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'salads' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'burritos' is clickable")
@allure.story("Проверка кнопки burritos")
def test_check_burritos_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку burritos"):
        burritos_button = page.get_by_role("button", name='Burritos')
        burritos_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Chicken Burrito", "Breakfast Burrito"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'burritos' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'smoothies' is clickable")
@allure.story("Проверка кнопки smoothies")
def test_check_smoothies_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку smoothies"):
        smoothies_button = page.get_by_role("button", name='smoothies')
        smoothies_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Red Velvet", "Blueberry Restorer",
                    "Island Tropics", "Healthy Glow"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'smoothies' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'bakery' is clickable")
@allure.story("Проверка кнопки bakery")
def test_check_bakery_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку bakery"):
        bakery_button = page.get_by_role("button", name='bakery')
        bakery_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Cinnamon Roll", "Iced Lemon Cake",
                    "Classic Coffee Cake", "Cream Cheese Danish",
                    "Blueberry Muffin", "Double Chocolate Chip Muffin",
                    "Chocolate Croissant", "Almond Croissant",
                    "Croissant", "Chocolate Cake Pop"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'bakery' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'bagels' is clickable")
@allure.story("Проверка кнопки bagels")
def test_check_bagels_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку bagels"):
        bagels_button = page.get_by_role("button", name='bagels')
        bagels_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Dozen Bagels", "Half Dozen Bagel Box",
                    "Poppy Seed Bagel", "Sesame Bagel",
                    "Potato Roll", "Honey Whole Wheat",
                    "Cinnamon Raisin Bagel", "Blueberry Bagel",
                    "Spinach Bagel", "Cinnamon Sugar Bagel",
                    "Plain Bagel", "Everything Bagel"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'bagels' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'coffee' is clickable")
@allure.story("Проверка кнопки coffee")
def test_check_coffee_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку coffee"):
        coffee_button = page.get_by_role("button", name='coffee')
        coffee_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Cold Brew Coffee", "Pumpkin Cream Cold Brew",
                    "Peppermint Mocha", "Salted Caramel Mocha",
                    "Frappè", "Cappuccino", "Flat White",
                    "Latte Macchiato", "Caffè Latte", "Mocha",
                    "Doppio", "Caffè Americano"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'coffee' is not clickable"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("Our menu functionality checking")
@allure.feature("Checking if the button 'tea' is clickable")
@allure.story("Проверка кнопки tea")
def test_check_tea_button(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(SelectorsMenuPage.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(SelectorsMenuPage.OUR_MENU_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step("Нажатие на кнопку tea"):
        tea_button = page.get_by_role("button", name='tea')
        tea_button.click()
        titles = page.query_selector_all(SelectorsMenuPage.DISHES)
        products = ["Ras Chai", "Earl Grey (Organic)", "Rooibos Bergamot",
                    "Moroccan Mint"]
        for i in range(len(titles)):
            assert titles[1].inner_text() == products[i], \
                "The button 'tea' is not clickable"
