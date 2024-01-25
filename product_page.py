import requests
from bs4 import BeautifulSoup


class Additional:
    def get_product_description(self, link):
        try:
            req = requests.get(link)
            req.raise_for_status()  # Raise an HTTPError for bad responses
            soup = BeautifulSoup(req.text, 'html.parser')
            desc = soup.find('div', {'id': 'tab-1'}).get_text(strip=True)
        except requests.RequestException as e:
            print(f"Error retrieving product description: {e}")
            desc = 'Нет информации!'
        except AttributeError as e:
            print(f"Error extracting product description: {e}")
            desc = 'Нет информации!'
        return desc

    def get_product_characteristics(self, link):
        try:
            req = requests.get(link)
            req.raise_for_status()  # Raise an HTTPError for bad responses
            soup = BeautifulSoup(req.text, 'html.parser')
            config = soup.find('div', {'id': 'tab-2'})
            config_item = config.find_all('tr')
            characteristics = {}
            for item in config_item:
                title = item.find('th').get_text(strip=True)
                info = item.find_next("td").get_text(strip=True)
                print(title)
                print(info)
                characteristics.update({title: info})
        except requests.RequestException as e:
            print(f"Error retrieving product characteristics: {e}")
            characteristics = {'info': 'Нет информации!'}
        except AttributeError as e:
            print(f"Error extracting product characteristics: {e}")
            characteristics = {'info': 'Нет информации!'}
        return characteristics
