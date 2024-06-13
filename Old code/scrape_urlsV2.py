import requests
from bs4 import BeautifulSoup

# Function to scrape the main page to gather the URls that contain the plant information.
def scrape_urls(main_page_url):
    # Variable with empty list to hold the retrieved urls needed to search for plant info
    url_list = []

    # using the argument passed into the function, this uses BeautifulSoup to capture the HTML
    main_page_to_scrape = requests.get(main_page_url)
    soup = BeautifulSoup(main_page_to_scrape.content, 'html.parser')

    # First, identify the parent container with the class name
    parent_container = soup.find('ul', class_='grid-products-list')
    # Then find all list items
    plant_items = parent_container.findAll('li')
    #
    filtered_items = [item for item in plant_items if any('item-' in cls for cls in item['class'])]

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
            url_list.append(full_url)
    # Returns the list of all URLs on the page
    return url_list

