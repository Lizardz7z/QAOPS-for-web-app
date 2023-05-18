from project_selectors.locators import SelectorsBasePage as Home
from Base import BasePage

class HomePage(BasePage):
    def home_link(self):
        self.follow_link(Home.HOME_PAGE_LINK)
