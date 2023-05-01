from pages import Base
from selectrs.locators import selectors_products_page


class products_page(Base):
    locators = selectors_products_page()
