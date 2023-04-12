from playwright.sync_api import sync_playwright
import selectors

def Test1(page, number):
    page.go('https://impresso-expresso.netlify.app/')
    page.go_products()
    page1 = selectors.Products_Page(page.page)
    page1.add_to_cart('//section/div/div/div/div/div/div/button', number)
    page1.go_cart()
    page1.check_prices('//*[@id="snipcart-items-list"]/tr/td[5]/span', number)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = selectors.Home_Page(browser.new_page())
        Test1(page, 3)

        browser.close()

if __name__=='__main__':
    main()