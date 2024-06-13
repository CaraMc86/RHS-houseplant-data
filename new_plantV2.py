import requests
from bs4 import BeautifulSoup


def get_plant_info(plantUrl):
    # Initialize variables to store plant information
    plant_name = None
    alt_name = None

    pageToScrape = requests.get(plantUrl)
    soup = BeautifulSoup(pageToScrape.text, 'html.parser')

    # Find the div with class "product-info" to capture the plant name
    product_info_div = soup.find('div', class_='product-info')

    # Find all h2 and h3 tags within the product_info_div as these hold the names - the specific plant name and the alt/latin name
    h2_h3_tags = product_info_div.find_all(['h2', 'h3'])

    # Extract text from the h2 and h3 tags if they exist
    for tag in h2_h3_tags:
        if tag.name == 'h2':
            plant_name = tag.text.strip()
        elif tag.name == 'h3':
            alt_name = tag.text.strip()

    # Find the height and spread for the given plant
    height_spread = soup.find('div', class_='plant-height-spread').text.strip().split('\n')
    eventual_height = height_spread[0].replace("Eventual height:", "").strip()
    eventual_spread = height_spread[1].replace("Eventual spread:", "").strip()

    # Find the span element with class "item-about-description"
    about_description_span = soup.find('span', class_='item-about-description')
    if about_description_span:
        list_items = about_description_span.find_all('li')

        # Extract text from each list item, filter li items based on the required keywords they start with and then remove these keywords prefixes to store in a variable.
        # This has been done as there are no attributes for the individual list items to target directly when scraping
        position_items = [li.get_text(strip=True).replace("Position:", "").strip() for li in list_items if
                          li.get_text(strip=True).startswith("Position:")]
        plant_position = position_items[0] if position_items else 'N/A'


        soil_items = [li.get_text(strip=True).replace("Soil:", "").strip() for li in list_items if
                      li.get_text(strip=True).startswith("Soil:")]
        soil_type = soil_items[0] if soil_items else 'N/A'

        growthRate_items = [li.get_text(strip=True).replace("Rate of growth:", "").strip() for li in list_items if
                      li.get_text(strip=True).startswith("Rate of growth:")]
        growth_rate = growthRate_items[0] if growthRate_items else 'N/A'


        hardiness_items = [li.get_text(strip=True).replace("Hardiness:", "").strip() for li in list_items if
                      li.get_text(strip=True).startswith("Hardiness:")]
        plant_hardiness = hardiness_items[0] if hardiness_items else 'N/A'

        # Extract text from each list item, filter items starting with "Home Care:", and remove "Home Care:" prefix to store in a variable
        homeCare_items = [li.get_text(strip=True).replace("Home care:", "").strip() for li in list_items if
                           li.get_text(strip=True).startswith("Home care:")]
        home_care = homeCare_items[0] if homeCare_items else 'N/A'

        hazards_span = soup.find('span', class_='item-poisonous')
        if hazards_span:
            hazard_li = hazards_span.find_all('li')
            hazard_items = [li.get_text(strip=True).replace('Humans/Pets:', '').strip() for li in hazard_li if
                            li.get_text(strip=True).startswith('Humans/Pets:')]
            plant_hazard = hazard_items[0]
        else:
            plant_hazard = 'N/A'


    # Return the extracted plant information
    return plant_name, alt_name, eventual_spread, eventual_height, plant_position, soil_type, growth_rate, plant_hardiness, home_care.replace('  ', ' '), plant_hazard

if __name__ == '__main__':
    plant1 = get_plant_info('https://www.rhsplants.co.uk/plants/_/dypsis-lutescens/classid.2000049004/')
    print(plant1)