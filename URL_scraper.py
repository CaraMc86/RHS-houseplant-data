import requests
from bs4 import BeautifulSoup as bs

class URLScraper:
    def __init__(self, source_url):
        """Initialise class attributes"""
        self.source_url = source_url
        self.soup = None
        self.url_list = []

    def fetch_url_content(self):
        """Retrieve and store all HTML content"""
        # use 'get' request to capture all html information of the page
        url_response = requests.get(self.source_url)
        # Parse the HTML content into the bs (beautifulSoup) object and assign to self.soup
        self.soup = bs(url_response.content, 'html.parser')

    def find_plant_items(self):
        """Locate parent container and individual list items"""
        # Use the find method to search for unordered lists with the relevant class using the soup object
        parent_container = self.soup.find('ul', class_='grid-products-list')
        # Then find all list items and store in self.plant_items
        self.plant_items = parent_container.findAll('li')

    def filter_plant_items(self):
        filtered_items = [item for item in self.plant_items if any('item-' in cls for cls in item['class'])]

        # for loop to go through all list items containing 'item-'
        for item in filtered_items:
            'checking if they are attributes with href tag'
            link = item.find('a', href=True)

            # url variable captures the url held within the html
            url = link['href']
            # These don't contain the whole link so concatenates the base url with the product specific part to capture the whole url
            # This is then appended to the variable url_list
            if 'collection' in url:
                continue
            if url.startswith('/plants/'):
                base_url = 'https://www.rhsplants.co.uk'
                full_url = base_url + url
                self.url_list.append(full_url)
        # Returns the list of all URLs on the page
        return self.url_list