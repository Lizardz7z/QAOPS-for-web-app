from playwright.sync_api import Page


class base_page:
    locators = None

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://impresso-expresso.netlify.app/"

    def wait(self, timeout=2000):
        self.page.wait_for_timeout(timeout)


