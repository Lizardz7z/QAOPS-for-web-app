from Base import BasePage
from project_selectors.locators import SelectorsProductsPage as Page
from project_selectors.locators import SelectorsCartPage as Cart


class Products(BasePage):
    def products_page(self):
        self.click_button(Page.PRODUCTS_PAGE_LINK)

    def products(self):
        return self.get_all(Page.ITEMS_SELECTOR)

    def product(self, commodity):
        return self.attribute(commodity, Cart.DATA_ITEM_NAME_ATTRIBUTE)

    def price(self, product):
        return float(self.attribute(product, Cart.DATA_ITEM_PRICE_ATTRIBUTE))

    def our_products(self):
        dictionary = {}
        products = self.products()
        for i in range(len(products)):
            dictionary[self.product(products[i])] = 0
        return dictionary

    def our_products_prices(self):
        dictionary = {}
        products = self.products()
        for i in range(len(products)):
            dictionary[self.product(products[i]).upper()] = self.price(products[i])
        return dictionary

    def close_button(self):
        self.click_button(Cart.CART_CLOSE_BUTTON)