
from playwright.sync_api import sync_playwright
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_functions as mf



prices_pymes = mf.read_json(r"..\\data\\prices_pymes.json")

def Sinterceros():
    products = []
    prices = []
    with sync_playwright() as p:
        browser =  p.chromium.launch(
        headless=True
        )
        page =  browser.new_page()
        page.goto("file:///D:/download/Download_Edge/Sinterceros.html")

        web_poducts =  page.locator("h3.font-medium")
        
        web_prices =  page.locator("p.font-medium")

        for i in range(web_poducts.count()):
          products.append(web_poducts.nth(i).inner_text())
        
        for j in range(web_prices.count()):
          prices.append(web_prices.nth(j).inner_text())
        
        prices_pymes["4"]["products"] = mf.list_to_dict(products, [ int(mf.you_type(''.join(mf.del_value(p[:-3],","))))  for p in prices])

        browser.close()

def Guamay():
    products = []
    prices = []
    scrap = []
    with sync_playwright() as p:
        browser =  p.chromium.launch(
        headless=True
        )
        page =  browser.new_page()
        page.goto("file:///D:/download/Download_Edge/MEGACARIBE%20Megacaribe%20-%20Higiene%20y%20Limpieza%20-%20Productos%20para%20el%20cabello.html")

        web_poducts =  page.locator("p.fw-bold")
   
        for i in range(web_poducts.count()):
          scrap.append(web_poducts.nth(i).inner_text())

        products = [ scrap[i].strip().replace("\\", "") for i in range(len(scrap)) if i % 2 == 0]
        prices = [ float(scrap[i][:-3][1:].strip())for i in range(len(scrap)) if i % 2 != 0]
        prices_pymes["8"]["products"].update(mf.list_to_dict(products, prices))
      
        browser.close()

def Cubanearme():
    products = []
    prices = []
    with sync_playwright() as p:
        browser =  p.chromium.launch(
        headless=True
        )
        page =  browser.new_page()
        page.goto("file:///D:/download/Download_Edge/Cubanearme%20S.R.L_mercado..html")

        web_poducts =  page.locator("a.link-nav-a")

        web_prices =  page.locator("p.price-offer")

        for i in range(web_poducts.count()):
          products.append(web_poducts.nth(i).inner_text().strip())
        
        for j in range(web_prices.count()):
          prices.append(float(web_prices.nth(j).inner_text().replace(',', '.')[:-3]))
        
        prices_pymes["9"]["products"].update(mf.list_to_dict(products, prices))
      
        browser.close()

if __name__ == "__main__":
    Cubanearme()
    mf.save_json(prices_pymes, r"..\\data\\prices_pymes.json")


  

