import requests
from bs4 import BeautifulSoup

# Function to scrape the main page to gather the URls that contain the plant infomration.
def scrape_urls(main_page_url):
    # Variable with empty list to hold the retrienved urls
    url_list = []

    main_page_to_scrape = requests.get(main_page_url)
    soup = BeautifulSoup(main_page_to_scrape.content, 'html.parser')

    parent_container = soup.find('ul', class_='grid-products-list')
    plant_items = parent_container.findAll('li')
    filtered_items = [item for item in plant_items if any('item-' in cls for cls in item['class'])]

    for item in filtered_items:
        link = item.find('a', href=True)
        url = link['href']
        if url.startswith('/plants/'):
            base_url = 'https://www.rhsplants.co.uk'
            full_url = base_url + url
            url_list.append(full_url)

    return url_list

if __name__ == '__main__':
    scrape_urls()