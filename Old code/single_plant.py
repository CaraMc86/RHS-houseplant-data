import requests
from bs4 import BeautifulSoup

def scrape_plant_info(url):
    # Fetch the webpage content
    pageToScrape = requests.get(url)
    soup = BeautifulSoup(pageToScrape.text, 'html.parser')

    # Find the div with class "product-info" to capture the plant name
    product_info_div = soup.find('div', class_='product-info')

    # Initialize dictionary to store plant information
    plant_info = {}

    # Find all h2 and h3 tags within the product_info_div as these hold the names - the specific plant name and the alt/latin name
    h2_h3_tags = product_info_div.find_all(['h2', 'h3'])

    # Extract text from the h2 and h3 tags if they exist
    for tag in h2_h3_tags:
        if tag.name == 'h2':
            plant_info['Plant name'] = tag.text.strip()
        elif tag.name == 'h3':
            plant_info['Alt name'] = tag.text.strip()

    # Find the height and spread for the given plant
    height_spread = soup.find('div', class_='plant-height-spread')
    if height_spread:
        height_spread_text = height_spread.text.strip().split('\n')
        plant_info['Eventual height'] = height_spread_text[0].strip()
        plant_info['Eventual spread'] = height_spread_text[1].strip()

    # Find the position, soil, rate of growth, hardiness, home care, and humans/pets information
    care_info = soup.find('ul', class_='plant-info-list')
    if care_info:
        for li in care_info.find_all('li'):
            key, value = li.text.split(':', 1)
            plant_info[key.strip()] = value.strip()

    return plant_info

# Example usage:
url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/'
plant_info = scrape_plant_info(url)
for key, value in plant_info.items():
    print(f'{key}: {value}')
