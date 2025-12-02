from playwright.sync_api import sync_playwright, Page, expect
from pathlib import Path

rute_chrome = Path.home() / "AppData" / "Local" / "ms-playwright" / "chromium-1187" / "chrome-win" / "chrome.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(
        # executable_path=rute_chrome,
        headless=True
    )
    page = browser.new_page()
    page.goto("https://sinterceros.com/akokan")
   # Ejemplo: localizar por font-medium
    first_product = page.locator("h3.font-medium")
    print(first_product.first.inner_text())
    first_price = page.locator("span.text-lg")
    print(first_price.inner_text())
    products = page.locator("h3.font-medium")
    for i in range(products.count()):
        print(products.nth(i).inner_text())

    browser.close()

if __name__ == "__main__":
    pass