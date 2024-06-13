from plantsConnect import *
from new_plantV3 import get_plant_info
from addPlantToDBV1 import add_plant_to_DB
from scrape_urlsV2 import scrape_urls
import sqlite3

main_page_url = 'https://www.rhsplants.co.uk/plants/_/indoor-plants/foliage-indoor-plants/plcid.20/plcid.285/numitems.100/sort.7/canorder.1/'

def getAll():
    try:
        # scrape the relevant urls from the main page using the scrape_url function
        # and the variable main_page_url as an argument
        plant_urls = scrape_urls(main_page_url)

        # Iterate over each plant for each url retrieved
        for plant_url in plant_urls:
            plant_info = get_plant_info(plant_url)
            add_plant_to_DB(plant_info)

        print('All plants added to the database successfully!')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    getAll()