

class BasePage:
    def __init__(self, page):
        self.page=page

    def go(self, link):
        self.page.goto(link)

    def follow_link(self, selector):
        link=self.page.query_selector(selector)
        link.click()

    def wait(self, timeout):
        self.page.wait_for_timeout(timeout)

class Home_Page(BasePage):
    def go_products(self):
        self.follow_link('[href="/products"]')

class Products_Page(BasePage):
    def add_to_cart(self, selector, number):
        products = self.page.query_selector_all(selector)
        close_button = self.page.query_selector('//*[@id="snipcart-close"]/i')
        for i in range(0,number):
            products[i].click()
            self.wait(4000)
            close_button.click()
            self.wait(2000)


