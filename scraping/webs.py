from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Users\Joswald\AppData\Local\ms-playwright\chromium-1187\chrome-win\chrome.exe",
        headless=True
    )
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())
    browser.close()

if __name__ == "__main__":
    pass