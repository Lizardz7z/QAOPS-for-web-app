from Base import BasePage
from project_selectors.locators import SelectorsCartPage as cart


class Cart(BasePage):
    def cart_page(self):
        self.click_button(cart.CART_PAGE_LINK)

    def products_in_cart(self):
        return self.get_all(cart.ITEMS_IN_CART)

    def product_name(self, selector):
        return self.locator(selector, cart.PRODUCT_NAME).inner_text()

    def quantity(self, selector):
        return self.locator(selector, cart.QUANTITY).inner_text()

    def sum(self):
        return self.get(cart.SUM_OF_PRODUCTS)

    def unit_price(self, selector):
        return self.locator(selector, cart.UNIT_PRICE)

    def total_price(self, selector):
        return self.locator(selector, cart.TOTAL_PRICE).inner_text()

    def delete_button(self):
        return self.get(cart.DELETE_ITEM_BUTTON)

    def empty_cart_message(self):
        return self.get(cart.EMPTY_CART).inner_text()

    def protect(self):
        return self.get(cart.PROTECT).inner_text()

    def next_step_1(self):
        return self.get(cart.NEXT_STEP_1)

    def previous_step(self):
        return self.get(cart.PREVIOUS_STEP)
