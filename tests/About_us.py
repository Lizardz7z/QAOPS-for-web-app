from project_selectors.locators import SelectorsAboutPage as About
from Base import BasePage


class AboutUsPage(BasePage):
    def about_us_link(self):
        self.follow_link(About.ABOUT_PAGE_LINK)

    def blocks(self):
        return self.get_all(About.BLOCKS)

