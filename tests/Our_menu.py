from Base import BasePage
from project_selectors.locators import SelectorsMenuPage


class MenuPage(BasePage):
    def menu_link(self):
        self.follow_link(SelectorsMenuPage.OUR_MENU_PAGE_LINK)

    def dishes(self):
        return self.get_all(SelectorsMenuPage.DISHES)

    def button(self, name):
        return self.role("button", name)

