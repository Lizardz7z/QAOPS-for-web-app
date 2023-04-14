class BasePage:
    def __init__(self, page):
        self.page=page

    def go(self, link):
        self.page.goto(link)

    def follow_link(self, selector):
        link=self.page.query_selector(selector)
        link.click()
        self.page.wait_for_timeout(2000)

    def go_cart(self):
        self.follow_link('//*[@id="gatsby-focus-wrapper"]/nav/div/ul/li[6]')

    def wait(self, timeout):
        self.page.wait_for_timeout(timeout)

class Home_Page(BasePage):
    def go_products(self):
        self.follow_link('[href="/products"]')

class Products_Page(BasePage):
    def add_to_cart(self, selector, number):
        products = self.page.query_selector_all(selector)
        close_button = self.page.query_selector('//*[@id="snipcart-close"]/i')
        for i in range(0, number):
            products[i].click()
            self.wait(2000)
            close_button.click()
            self.wait(1000)

    def check_prices(self, selector, number):
        prices=self.page.query_selector_all(selector)
        sum=0.0
        for i in range(0, number):
            s=prices[0].inner_text()
            sn=s[1:]
            a=float(sn)
            sum+=a
        sumofproducts=self.page.query_selector('//*[@id="snipcart-amount"]')
        s1=sumofproducts.inner_text()
        s1n=s1[1:]
        a1=float(s1n)
        assert a1==sum
