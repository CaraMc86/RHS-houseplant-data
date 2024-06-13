import requests
from bs4 import BeautifulSoup

# Search main page for the HTML content
main_page_to_scrape = requests.get('https://www.rhsplants.co.uk/plants/_/indoor-plants/foliage-indoor-plants/plcid.20/plcid.285/numitems.100/sort.7/canorder.1/')
soup = BeautifulSoup(main_page_to_scrape.content, 'html.parser')
# Verify HTML parsing works.
# print(soup)

parent_container = soup.find('ul', class_='grid-products-list')
# Verify parent container
# print(parent_container)

plant_items = parent_container.findAll('li')
# print(plant_items)

for item in plant_items:
    print(item['class'])

filtered_items = [item for item in plant_items if any('item-' in cls for cls in item['class'])]

print(f'Number of filtered plant items: {len(filtered_items)}')

# # Dictionary to hold the URLs
# url_dict = {}
#
# # Creating the variable plant_items to find all list elements within the parsed HTML
# # class_ to search for elements with a specific class name
# # Used th lambda function as only ned this temporarily - as a filter
# # x is the defined parameter to represent the class names
# # The expression checks if any class name in `x` contains 'item-' (the function checks each class name in the list).
# # This line essentially captures any li items with a class containing 'item-'
# plant_items = soup.find_all('li', class_=lambda x: x and any('item-' in cls for cls in x))
# print(plant_items)
# for item in plant_items:
#     # item['class'] - accesses the classes with the identified expression
#     # [1] indexes into the list of class names to access the *second* class name - in this case
#     section_number = item['class'][1].split('-')[1]
#     if section_number not in url_dict:
#         link = item.find('a', href=True)
#         url = link['href']
#         if url.startswith('/plants/'):
#             base_url = 'https://www.rhsplants.co.uk'
#             full_url = base_url + url
#             url_dict[section_number] = full_url
#
# for section, url in url_dict.items():
#     print(f'Section {section}: {full_url}')