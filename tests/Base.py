class BasePage:

    def __init__(self, page):
        self.page = page

    def get(self, selector):
        return self.page.query_selector(selector)

    def get_all(self, selector):
        return self.page.query_selector_all(selector)

    def wait(self, timeout=2000):
        self.page.wait_for_timeout(timeout)

    def follow_link(self, link):
        self.page.goto(link)
        self.page.wait_for_timeout(2000)

    def value(self, selector):
        return self.page.input_value(selector)

    def role(self, obj, name):
        return self.page.get_by_role(obj, name=name)

    def attribute(self, obj, selector):
        return obj.get_attribute(selector).upper()

    def click_button(self, selector):
        close_button = self.get(selector)
        close_button.click()
        self.wait()

    def locator(self, selector1, selector2):
        return selector1.query_selector(selector2)
