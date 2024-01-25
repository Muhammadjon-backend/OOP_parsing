from bs4 import BeautifulSoup
import requests
import json

class BaseParser:
    def __init__(self):
        self.BASE_URL = 'https://upg.uz'
        self.HOST = 'https://upg.uz'
        self.url = 'https://upg.uz'
        self.host = 'https://upg.uz'


    def get_html(self, url=None):
        try:
            if url:
                html = requests.get(url).text
            else:
                html = requests.get(self.BASE_URL).text
            return html
        except requests.RequestException as e:
            print(f"Error fetching HTML content: {e}")
            return None

    def get_soup(self, html):
        try:
            return BeautifulSoup(html, 'html.parser')
        except Exception as e:
            print(f"Error creating BeautifulSoup object: {e}")
            return None

    @staticmethod
    def save_json(filename, data):
        with open(f"{filename}.json", mode="w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
