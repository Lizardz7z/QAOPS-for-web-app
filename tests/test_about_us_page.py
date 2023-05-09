import pytest
import allure

from selectrs.locators import selectors_about_page

browsers = ['setup_browser_chrome', 'setup_browser_firefox']


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("About us functionality checking")
@allure.feature("Сhecking the display of text in block 1")
@allure.story("Проверка отображения текста в блоке 1")
def test_check_block_1(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_about_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step('Проверка 1 блока'):
        blocs = page.query_selector_all(selectors_about_page.BLOCKS)
        assert blocs[0].inner_text() == "We - we roast coffee. Craft of coffee " \
                                        "roasting " \
                                        "is what we know best. We demand the same " \
                                        "levels " \
                                        "of commitment to know-how from all of the " \
                                        "people " \
                                        "we work with. The result of this mutual " \
                                        "understanding " \
                                        "is a full-flavoured, balanced, and easily " \
                                        "recognizable " \
                                        "taste of our coffees. We source and buy green " \
                                        "coffees " \
                                        "directly from farmers.", \
                                        "Block 1 is not displayed"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("About us functionality checking")
@allure.feature("Сhecking the display of text in block 2")
@allure.story("Проверка отображения текста в блоке 2")
def test_check_block_2(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_about_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step('Проверка 2 блока'):
        blocs = page.query_selector_all(selectors_about_page.BLOCKS)
        assert blocs[1].inner_text() == "We love coffee. Coffee bean is fascinating. " \
                                        "There is nothing that simple and yet that " \
                                        "difficult " \
                                        "at the same time. Coffee is a multicultural " \
                                        "phenomenon, " \
                                        "a language understandable by most people " \
                                        "on earth. " \
                                        "Coffee is a good with a very complex character, " \
                                        "multi-faceted, unpredictable. Coffee opens " \
                                        "up only " \
                                        "to those who devote to it a lot of time " \
                                        "and energy, " \
                                        "those who ponder over it and admire it.", \
                                        "Block 2 is not displayed"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("About us functionality checking")
@allure.feature("Сhecking the display of text in block 3")
@allure.story("Проверка отображения текста в блоке 3")
def test_check_block_3(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_about_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step('Проверка 3 блока'):
        blocs = page.query_selector_all(selectors_about_page.BLOCKS)
        assert blocs[2].inner_text() == "In specialty coffee culture an ability to " \
                                        "properly brew coffee is summing it all up. " \
                                        "In one cup of coffee we bring together " \
                                        "efforts " \
                                        "of all of those who worked on the taste " \
                                        "of that cup. " \
                                        "Efforts by farmers, pickers, those who " \
                                        "processed, " \
                                        "sorted and graded the coffee, " \
                                        "cuppers, roasters.", \
                                        "Block 3 is not displayed"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("About us functionality checking")
@allure.feature("Сhecking the display of text in block 4")
@allure.story("Проверка отображения текста в блоке 4")
def test_check_block_4(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_about_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step('Проверка 4 блока'):
        blocs = page.query_selector_all(selectors_about_page.BLOCKS)
        assert blocs[3].inner_text() == 'Coffee is a ritual, a small treat ' \
                                        'in the morning, "fuel", a break, chat, ' \
                                        'affair that makes up our lives. Making ' \
                                        'the coffee better, we make our lives better. ' \
                                        'With this concept in mind, our blends were developed ' \
                                        'by the leading professionals in the coffee industry.', \
                                        "Block 4 is not displayed"


@pytest.mark.parametrize('setup_browser', browsers)
@pytest.mark.fast
@allure.feature("About us functionality checking")
@allure.feature("Сhecking the display of text in block 5")
@allure.story("Проверка отображения текста в блоке 5")
def test_check_block_5(setup_browser, request):
    with allure.step("Запуск браузера и открытие страницы"):
        page = request.getfixturevalue(setup_browser)
        page.goto(selectors_about_page.PAGE_LINK)
        page.wait_for_timeout(2000)
        link = page.query_selector(selectors_about_page.ABOUT_PAGE_LINK)
        link.click()
        page.wait_for_timeout(2000)
    with allure.step('Проверка 5 блока'):
        blocs = page.query_selector_all(selectors_about_page.BLOCKS)
        assert blocs[4].inner_text() == 'Strive for learning new things creates ' \
                                        'a forward movement, a self-improvement. ' \
                                        'Beauty of coffee is that it is an ' \
                                        'inexhaustible ' \
                                        'source of knowledge for all of those ' \
                                        'who engage ' \
                                        'with this product. Our daily work with ' \
                                        'green and ' \
                                        'roasted coffee provides us with ' \
                                        'experience and ' \
                                        'encourages us to constantly search ' \
                                        'and gather ' \
                                        'more knowledge from coffee growers, ' \
                                        'baristas and ' \
                                        'other roasters. All the knowledge ' \
                                        'we accumulate ' \
                                        'we invest in our coffees!', \
                                        "Block 5 is not displayed"