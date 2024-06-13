import requests
from bs4 import BeautifulSoup as bs

class GetPlant:

    def __init__(self, url):
        """Initialise GetPlant class attributes"""
        self.url = url
        self.soup = None
        self.plant_name = None
        self.alt_plant_name = None
        self.height = None
        self.spread = None
        # Initialising about_list_items as an empty list
        self.about_list_items = []
        self.position = None
        self.soil = None
        self.growthRate = None
        self.hardiness = None
        self.homeCare = None

    def get_url_info(self):
        """Method to parse HTML from URL to be used in other methods"""
        pageToScrape = requests.get(self.url)
        self.soup = bs(pageToScrape.text, 'html.parser')

    def get_plant_name(self):
        """Method to isolate the plant name"""
        plant_info_div = self.soup.find('div', class_='product-info')
        plant_name_tag = plant_info_div.find('h2')

        if plant_name_tag:
            self.plant_name = plant_name_tag.text.strip()
            return self.plant_name
        else:
            return None
    def get_alt_plant_name(self):
        """Method to return the alt name"""
        plant_info_div = self.soup.find('div', class_='product-info')
        alt_plant_name_tag = plant_info_div.find('h3')

        if alt_plant_name_tag:
            self.alt_plant_name = alt_plant_name_tag.text.strip()
            return self.alt_plant_name
        else:
            return None

    def get_height(self):
        """Method to return the eventual plant height"""
        # Use the soup object to find the div with the class 'plant-height-spread-text'.
        # Once found, use find again with the Lambda 'anonymous' function.
        # The lambda function takes t, representing text in the li element,
        # and checks if 'Eventual height' is in t as the search criteria to find any li including this text
        height_li = self.soup.find('div', class_='plant-height-spread-text').find('li', text=lambda t: 'Eventual height' in t)
        # If any li items is found matching this descriptor, we assign to the self.height object and clean the text.
        if height_li:
            self.height = height_li.get_text(strip=True).replace('Eventual height:', '').strip()
        else:
            self.height = None
        return self.height

    def get_spread(self):
        """Method to return the eventual plant spread - the same methodology as get_height applies"""
        spread_li = self.soup.find('div', class_='plant-height-spread-text').find('li', text=lambda t: 'Eventual spread' in t)
        if spread_li:
            self.spread = spread_li.get_text(strip=True).replace('Eventual spread:', '').strip()
        else:
            self.spread = None
        return self.spread

    def get_about_info(self):
        """Method to find and extract the wider "item-about-description" class"""
        about_description_span = self.soup.find('span', class_='item-about-description')
        self.about_list_items = about_description_span.find_all('li')

    def _get_position(self):
        # Checks for initialisation
        if self.position is None:
            # Perform the extraction and cleaning of position information.
            # The occurs by
            self.position = [li.get_text(strip=True).replace("Position:", "").strip() for li in self.about_list_items if
                             li.get_text(strip=True).startswith("Position:")]
            self.position = self.position[0] if self.position else 'N/A'
            self.position = str(self.position)
        return self.position

    def _get_soil(self):
        if self.soil is None:
            self.soil = [li.get_text(strip=True).replace("Soil:", "").strip() for li in self.about_list_items if
                             li.get_text(strip=True).startswith("Soil:")]
            self.soil = self.soil[0] if self.soil else 'N/A'
            self.soil = str(self.soil)
            return self.soil

    def _get_growthRate(self):
        if self.growthRate is None:
            self.growthRate = [li.get_text(strip=True).replace("Rate of growth:", "").strip() for li in self.about_list_items if
                             li.get_text(strip=True).startswith("Rate of growth:")]
            self.growthRate = self.growthRate[0] if self.growthRate else 'N/A'
            self.growthRate = str(self.growthRate)
            return self.growthRate

    def _get_homeCare(self):
        if self.homeCare is None:
            self.homeCare = [li.get_text(strip=True).replace("Home care:", "").strip().replace("  ", " ").strip() for li in self.about_list_items if
                             li.get_text(strip=True).startswith("Home care:")]
            self.homeCare = self.homeCare[0] if self.homeCare else 'N/A'
            self.homeCare = str(self.homeCare)
            return self.homeCare


