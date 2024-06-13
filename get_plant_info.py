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


    #     if about_description_span:
    #         list_items = about_description_span.find_all('li')
    #
    #         # Extract text from each list item, filter li items based on the required keywords they start with and then remove these keywords prefixes to store in a variable.
    #         # This has been done as there are no attributes for the individual list items to target directly when scraping
    #         position_items = [li.get_text(strip=True).replace("Position:", "").strip() for li in list_items if
    #                           li.get_text(strip=True).startswith("Position:")]
    #         plant_position = position_items[0] if position_items else 'N/A'
    #         print(f'Plant Position {plant_position}')
    #
    #         soil_items = [li.get_text(strip=True).replace("Soil:", "").strip() for li in list_items if
    #                       li.get_text(strip=True).startswith("Soil:")]
    #         soil_type = soil_items[0] if soil_items else 'N/A'
    #         print(f'Soil Type {soil_type}')
    #
    #         growthRate_items = [li.get_text(strip=True).replace("Rate of growth:", "").strip() for li in list_items if
    #                             li.get_text(strip=True).startswith("Rate of growth:")]
    #         growth_rate = growthRate_items[0] if growthRate_items else 'N/A'
    #         print(f'Growth rate: {growth_rate}')
    #
    #         hardiness_items = [li.get_text(strip=True).replace("Hardiness:", "").strip() for li in list_items if
    #                            li.get_text(strip=True).startswith("Hardiness:")]
    #         plant_hardiness = hardiness_items[0] if hardiness_items else 'N/A'
    #         print(f'Hardiness: {plant_hardiness}')
    #
    #         # Extract text from each list item, filter items starting with "Home Care:", and remove "Home Care:" prefix to store in a variable
    #         homeCare_items = [li.get_text(strip=True).replace("Home care:", "").strip() for li in list_items if
    #                           li.get_text(strip=True).startswith("Home care:")]
    #         home_care = homeCare_items[0] if homeCare_items else 'N/A'
    #         print(f'Home Care: {home_care}')
    #
    #         hazards_span = soup.find('span', class_='item-poisonous')
    #         if hazards_span:
    #             hazard_li = hazards_span.find_all('li')
    #             for li in hazard_li:
    #                 # Check if the text starts with any of the specified prefixes
    #                 if li.get_text(strip=True).startswith(('Humans/Pets:', 'Pets:', 'Humans:')):
    #                     plant_hazard = li.get_text(strip=True).strip()
    #                     break  # Exit the loop once a match is found
    #             else:
    #                 plant_hazard = 'N/A'  # Set default value if no match is found
    #         else:
    #             plant_hazard = 'N/A'
    #         print(f'Hazards: {plant_hazard}')
