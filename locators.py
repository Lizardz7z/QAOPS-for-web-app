class Selectors:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/'
    HOME_PAGE_LINK = '//*[@id="gatsby-focus-wrapper"]/nav/div/ul/li[1]/a'
    HOME_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div[1]/h1'
    OUR_MENU_PAGE_LINK = '[href="/menu"]'
    OUR_MENU_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'
    PRODUCTS_PAGE_LINK = '[href="/products"]'
    PRODUCTS_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'
    ABOUT_PAGE_LINK = '[href="/about"]'
    ABOUT_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'
    CONTACTUS_PAGE_LINK = '[href="/contact"]'
    CONTACTUS_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'
    CART_PAGE_LINK = '//*[@id="gatsby-focus-wrapper"]/nav/div/ul/li[6]'
    CART_PAGE_TITLE = '//*[@id="snipcart-title"]'
    ITEMS_SELECTOR = '//section/div/div/div/div/div/div/button'
    CART_CLOSE_BUTTON = '//*[@id="snipcart-close"]/i'
    CART_CHECKOUT = '//*[@id=snipcart-checkout-step]/i'
    SUM_OF_PRODUCTS = '//*[@id="snipcart-amount"]'
    DATA_ITEM_PRICE_ATTRIBUTE = "data-item-price"
    DATA_ITEM_NAME_ATTRIBUTE = "data-item-name"
    ITEMS_IN_CART = '.snip-table__item'
    QUANTITY = ".snip-quantity-trigger__text"
    PRODUCT_NAME = ".snip-product__name"
    UNIT_PRICE = '[data-bind="unitPrice"]'
    TOTAL_PRICE = '[data-bind="totalPrice"]'

