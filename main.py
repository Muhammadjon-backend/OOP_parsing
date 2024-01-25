from time import time
from baseparser import BaseParser
from product_page import Additional
import json
from database import (
    insert_category,
    get_category_id,
    get_product_id,
    insert_product_data,
    insert_characteristic,
)


class OOP_parser(BaseParser, Additional):
    def __init__(self):
        super(OOP_parser, self).__init__()
        self.data = {}
        # Бонус в виде json дынных из видео

    def get_data(self):
        soup = self.get_soup(self.get_html())
        filter_item = soup.find('div', class_='fi-tablet-left')
        categories = filter_item.find_all('li', class_='dropdown-submenu')
        for category in categories:
            category_title = category.find('a').get_text(strip=True)
            category_link = category.find('a').get('href')
            print(category_title)
            print(category_link)

            insert_category(category_title, category_link)

            self.get_products_page(category_title, category_link)

    def get_products_page(self, category_title, category_link):
        category_id = get_category_id(category_title)
        soup = self.get_soup(self.get_html(category_link))
        product_grid = soup.find('div', class_='product-grid')
        products = product_grid.find_all('div', class_='item-product')
        for product in products[:3]:
            product_title = product.find('a', class_='item-link').get_text(strip=True)
            product_link = product.find('a', class_='item-link').get('href')
            print(product_title)
            print(product_link)
            try:
                product_price = product.find('span', class_='item-price').get_text(strip=True)
                product_price = int(product_price.replace(' ', '').replace('сум', ''))
            except Exception as e:
                print(f"Error extracting product price: {e}")
                product_price = 0

            product_image = self.HOST + product.find('img').get('src')
            print(product_image)

            desc = self.get_product_description(link=product_link)
            insert_product_data(category_id, product_title, product_link, product_price, product_image, desc)

            product_id = get_product_id(product_title)

            characteristics = self.get_product_characteristics(link=product_link)
            insert_characteristic(product_id, characteristics)

    def category_page_parser(self, category_title, category_link):
        html = self.get_html(category_link)
        soup = self.get_soup(html)
        products = soup.find_all("div", class_="item-product-inner")
        for product in products:
            title = product.find("a").get_text(strip=True)
            price = product.find("span", class_="item-price price-new").get_text(strip=True)
            image = self.host + product.find("img").get("src")
            link = product.find("a").get("href")
            product_html = self.get_html(link)
            product_soup = self.get_soup(product_html)

            description = product_soup.find("div", id="tab-1").get_text(strip=True)

            self.data[category_title].append({
                "Наименование товара": title,
                "Цена товара": price,
                "Изображение": image,
                "Ccылки на товар": link,
                "Описание товара": description
            })


def start_parsing():
    start = time()
    try:
        parser = OOP_parser()
        parser.get_data()
        parser.save_json("electronics", parser.data)
    except Exception as e:
        print(f"Error during parsing: {e}")
    finally:
        finish = time()
        print(f"Парсер отработал за {finish - start} секунд")


start_parsing()
