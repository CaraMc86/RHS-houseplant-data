import requests
from bs4 import BeautifulSoup as bs

class GetPlant:

    def __init__(self, url):
        """Initialise GetPlant class attributes"""
        self.url = url
        self.soup = None
        self.plant_name = None
        self.alt_plat_name = None

    def get_url_info(self):
        pageToScrape = requests.get(self.url)
        self.soup = bs(pageToScrape.text, 'html.parser')

    def get_plant_name(self):
        plant_info_div = self.soup.find('div', class_='product-info')
        plant_name_tag = plant_info_div.find('h2')

        if plant_name_tag:
            self.plant_name = plant_name_tag.text.strip()
            return self.plant_name
        else:
            return None
    def get_alt_plant_name(self):
        plant_info_div = self.soup.find('div', class_='product-info')
        alt_plant_name_tag = plant_info_div.find('h3')

        if alt_plant_name_tag:
            self.plant_name = alt_plant_name_tag.text.strip()
            return self.plant_name
        else:
            return None

