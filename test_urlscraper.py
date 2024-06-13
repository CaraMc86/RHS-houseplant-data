import pytest
from URL_scraper import URLScraper

@pytest.fixture
def scraper():
    """Fixture function that returns an instance of URLScraper initialized with the test URL
    Creates and initialises an instance of URL scraper hat can be used in the subsequent tests.
    Used for consistency and to avoid duplication"""

    return URLScraper('https://www.rhsplants.co.uk/plants/_/indoor-plants/foliage-indoor-plants/plcid.20/plcid.285/numitems.100/sort.7/canorder.1/')

def test_fetch_url_content(scraper):
    """Test function to verify the fetch_url_content method"""
    # Call fetch_url_content method using the scraper instance
    scraper.fetch_url_content()
    # Assert that the 'soup' attribute of the scraper instance is not None,
    # indicating successful fetching and parsing of HTML content but checking that the returned 'scraper.soup is not none
    assert scraper.soup is not None


def test_find_plant_items(scraper):
    """Test function to verify the find_plant_items method"""
    # Call fetch_url_content method from scraper instance - already verified as working
    scraper.fetch_url_content()
    # Then call the find_plant_items method on the scraper instance to locate plant items
    scraper.find_plant_items()
    # Assert that the plant_items attribute of the scraper instance is populated,
    # indicating successful extraction of plant items from the HTML content
    assert len(scraper.plant_items) > 0

def test_filter_plant_items(scraper):
    """Test function to verify the filter_plant_items method"""
    # Call the fetch_url_content method on the scraper instance
    scraper.fetch_url_content()
    # Call the find_plant_items method on the scraper instance to locate plant items
    scraper.find_plant_items()
    # Call the filter_plant_items method on the scraper instance to filter plant items
    scraper.filter_plant_items()
    # Assert that the url_list attribute of the scraper instance contains items,
    # indicating successful filtering and extraction of URLs
    assert len(scraper.url_list) > 0
    # You can add further assertions here to validate specific URLs or properties
    # within the url_list attribute

# This block ensures that the tests are run when executing the script directly
if __name__ == "__main__":
    pytest.main()
