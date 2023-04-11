from playwright.sync_api import sync_playwright
import selectors

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = selectors.Home_Page(browser.new_page())
        page.go('https://impresso-expresso.netlify.app/')
        page.go_products()
        page.wait(5000)
        page1=selectors.Products_Page(page.page)
        page1.add_to_cart('//section/div/div/div/div/div/div/button', 3)
        browser.close()

if __name__=='__main__':
    main()