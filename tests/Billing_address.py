from Base import BasePage
from project_selectors.locators import SelectorsBillingAddress as Sba
from project_selectors.locators import SelectorsCartPage as Cart


class BillingAddress(BasePage):
    def name(self):
        return self.get(Sba.NAME)

    def name_value(self):
        return self.value(Sba.NAME)

    def company(self):
        return self.get(Sba.COMPANY)

    def company_value(self):
        return self.value(Sba.COMPANY)

    def address(self):
        return self.get(Sba.ADDRESS1)

    def address_value(self):
        return self.value(Sba.ADDRESS1)

    def address2(self):
        return self.get(Sba.ADDRESS2)

    def address2_value(self):
        return self.value(Sba.ADDRESS2)

    def city(self):
        return self.get(Sba.CITY)

    def city_value(self):
        return self.value(Sba.CITY)

    def zip(self):
        return self.get(Sba.ZIP)

    def zip_value(self):
        return self.value(Sba.ZIP)

    def phone(self):
        return self.get(Sba.PHONE)

    def phone_value(self):
        return self.value(Sba.PHONE)

    def email(self):
        return self.get(Sba.EMAIL)

    def email_value(self):
        return self.value(Sba.EMAIL)

    def country(self):
        return self.get(Sba.COUNTRY)

    def province(self):
        return self.get(Sba.PROVINCE)

    def next_step_2(self):
        return self.get(Cart.NEXT_STEP_2)