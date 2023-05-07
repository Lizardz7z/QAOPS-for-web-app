class selectors_base_page:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/'
    HOME_PAGE_LINK = '//*[@id="gatsby-focus-wrapper"]/nav/div/ul/li[1]/a'
    HOME_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div[1]/h1'
    COMMUNITY_TITLE = '//*[@id="gatsby-focus-wrapper"]/section[1]/div/div[1]/div/h1'
    COFFEE_TITLE = '//*[@id="gatsby-focus-wrapper"]/section[2]/div/div[1]/div/h1'
    CUSTOMER_TITLE = '//*[@id="gatsby-focus-wrapper"]/div[2]/div/div[1]/div/h1'



class selectors_menu_page:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/menu'
    OUR_MENU_PAGE_LINK = '[href="/menu"]'
    OUR_MENU_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'


class selectors_products_page:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/products'
    ITEMS_SELECTOR = '//section/div/div/div/div/div/div/button'
    PRODUCTS_PAGE_LINK = '[href="/products"]'
    PRODUCTS_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'


class selectors_about_page:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/about'
    ABOUT_PAGE_LINK = '[href="/about"]'
    ABOUT_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'


class selectors_contact_page:
    PAGE_LINK = 'https://impresso-expresso.netlify.app/contact'
    CONTACTUS_PAGE_LINK = '[href="/contact"]'
    CONTACTUS_PAGE_TITLE = '//*[@id="gatsby-focus-wrapper"]/div/h1'
    ITEMS_SELECTOR = '//section/div/div/div/div/div/div/button'


class selectors_cart_page:
    CART_PAGE_LINK = '//*[@id="gatsby-focus-wrapper"]/nav/div/ul/li[6]'
    CART_PAGE_TITLE = '//*[@id="snipcart-title"]'
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
    NEXT_STEP_1 = '//*[@id="snipcart-actions"]/a'
    NEXT_STEP_2 = '//*[@id="snipcart-next"]'


class selectors_billing_address:
    NAME = '//*[@id="snip-name"]'
    COMPANY = '//*[@id="snip-company"]'
    ADDRESS1 = '//*[@id="snip-address1"]'
    ADDRESS2 = '//*[@id="snip-address2"]'
    CITY = '//*[@id="snip-city"]'
    ZIP = '//*[@id="snip-postalCode"]'
    PHONE = '//*[@id="snip-phone"]'
    EMAIL = '//*[@id="snip-email"]'
    COUNTRY = '//*[@id="snip-country"]'
    PROVINCE = '//*[@id="snipprovince"]'

class selectors_footer:
    CONTACT_TITLE = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[1]/h5'
    OPEN_HOURS = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[2]/h5'
    SITE_LINKS = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/h5'
    HOME = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/ul/li[1]/a'
    MENU = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/ul/li[2]/a'
    PRODUCTS = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/ul/li[3]/a'
    ABOUT = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/ul/li[4]/a'
    CONTACT_LINK = '//*[@id="gatsby-focus-wrapper"]/footer/div/div/div[3]/ul/li[5]/a'
