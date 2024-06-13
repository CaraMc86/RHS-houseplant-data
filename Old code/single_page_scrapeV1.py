import requests
from bs4 import BeautifulSoup
from pprint import pprint

pageToScrape = requests.get('https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/')
soup = BeautifulSoup(pageToScrape.text, 'html.parser')

# Find the div with class "product-info" to capture the plant name
product_info_div = soup.find('div', class_='product-info')

# Find all h2 and h3 tags within the product_info_div as these hold the names - the specific plant name and the alt/latin name
h2_h3_tags = product_info_div.find_all(['h2', 'h3'])

# Extract text from the h2 and h3 tags if they exist
for tag in h2_h3_tags:
    if tag.name == 'h2':
        print(f'Plant name: {tag.text.strip()}')
    elif tag.name == 'h3':
        print(f'Alt name: {tag.text.strip()}')


# Find the height and spread for the given plant
height_spread = soup.findAll('div', attrs={'class':'plant-height-spread'})
for item in height_spread:
    # Strip leading and trailing whitespace
    text = item.text.strip()
    # Only process non-blank lines
    if text:
        print(text)

# Find the span containing all 'about' information.
# This is held within a span, with pseudo-elements seperating out the list items
plant_description = soup.find('span', class_='item-about-description')


if plant_description:
    # Checks to find all <li> elements within the span
    list_items = plant_description.findAll('li')
    for item in list_items:
        # For loop to strip leading and trailing whitespace taken up by the non-text HTML structure
        text = item.text.strip()
        # Only return non-blank lines - this also maintains the list structure.
        if text:
            print(text)