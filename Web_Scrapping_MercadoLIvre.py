from openpyxl import Workbook
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re


product_list = []


wb = Workbook()
ws = wb.create_sheet(title="Mercado_Livre_Products")
wb.remove(wb["Sheet"])


search_query = "notebook 16gb RAM and 1TB SSD"


browser = webdriver.Chrome()
browser.get("https://www.mercadolivre.com.br")
browser.maximize_window()

sleep(2)


search_button = browser.find_element(By.ID, "cb1-edit")
search_button.click()
search_button.send_keys(search_query)
search_button.send_keys(Keys.ENTER)

sleep(5)


html = browser.page_source
soup = BeautifulSoup(html, "html.parser")


products = soup.find_all("div", attrs={"class": "ui-search-result__wrapper"})


for product in products:

    if len(product_list) >= 20:
        break

    brand_tag = product.find("span", attrs={"class": "poly-component__brand"})
    brand = brand_tag.text if brand_tag else ""

    seller = ""
    name = ""

    link_tag = product.find("a", attrs={"class": "poly-component__title"})
    link = link_tag["href"] if link_tag else ""

    if link:
        browser.get(link)
        sleep(2)

        product_html = browser.page_source
        product_soup = BeautifulSoup(product_html, "html.parser")

        seller_tag = product_soup.find(
            "h2",
            attrs={
                "class": "ui-pdp-color--BLACK ui-pdp-size--LARGE "
                         "ui-pdp-family--SEMIBOLD ui-seller-data-header__title non-selectable"
            }
        )
        seller = seller_tag.text.strip() if seller_tag else ""

        name_tag = product_soup.find("h1", class_="ui-pdp-title")
        name = name_tag.text.strip() if name_tag else ""

    price_tag = product.find("span", attrs={"class": "andes-money-amount__fraction"})
    price = price_tag.text.strip() if price_tag else ""
    price = price.replace(",", ".")
    price = re.sub(r"[^\d.]", "", price)

    rating_tag = product.find("span", attrs={"class": "polyreviews__rating"})
    rating = rating_tag.text.strip() if rating_tag else ""
    rating = rating.replace(",", ".")
    rating = re.sub(r"[^\d.]", "", rating)

    product_data = {
        "Brand": brand,
        "Name": name,
        "Seller": seller,
        "Price": price,
        "Rating": rating
    }

    product_list.append(product_data)

    print(f"\n{product_data}")
    browser.back()


ws.append(["Brand", "Name", "Seller", "Price", "Rating"])

for product in product_list:
    ws.append([
        str(product["Brand"]),
        str(product["Name"]),
        str(product["Seller"]),
        float(product["Price"]) if product["Price"] else 0.0,
        str(product["Rating"])
    ])

print(f"Total products collected: {len(product_list)}")

wb.save("Mercado_Livre_Products.xlsx")
browser.quit()
