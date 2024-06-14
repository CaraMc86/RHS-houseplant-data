from url_scraper import URLScraper
from get_plant_info import GetPlant

class AddToDB:

    def __init__(self, url_scraper_instance, get_plant_instance):
        self.url_scraper = url_scraper_instance
        self.get_plant = get_plant_instance







if __name__ = '__main__':

    source_url = 'https://www.rhsplants.co.uk/plants/_/indoor-plants/foliage-indoor-plants/plcid.20/plcid.285/numitems.100/sort.7/canorder.1/'

    url_scraper = URLScraper(source_url)
    get_plant = GetPlant(url='')
