from Base import BasePage
from project_selectors.locators import SelectorsContactPage as Contact


class ContactUsPage(BasePage):
    def contact_us_link(self):
        self.follow_link(Contact.CONTACTUS_PAGE_LINK)

    def get_name(self):
        return self.get(Contact.NAME)

    def name_value(self):
        return self.value(Contact.NAME)

    def get_email(self):
        return self.get(Contact.EMAIL)

    def email_value(self):
        return self.value(Contact.EMAIL)

    def get_description(self):
        return self.get(Contact.DESCRIPTION)

    def description_value(self):
        return self.value(Contact.DESCRIPTION)