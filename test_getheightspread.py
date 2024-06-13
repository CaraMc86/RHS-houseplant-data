import pytest
from get_plant_info import GetPlant

# Define a fixture to instantiate GetPlant with the URL
@pytest.fixture
def plant_info():
    url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/'
    return GetPlant(url)

# Test case to fetch and validate the plant height
def test_get_height(plant_info):
    # Fetch HTML content and parse with BeautifulSoup
    plant_info.get_url_info()

    # Retrieve the plant height
    plant_height = plant_info.get_height()

    # Assert that the plant height is not None (indicating it was found)
    assert plant_height is not None, "Plant height should not be None"

    # Assert specific expected values if known
    expected_plant_height = "2.5m"
    assert plant_height == expected_plant_height, f"Expected plant height '{expected_plant_height}', got '{plant_height}'"

# Test case to fetch and validate the plant spread
def test_get_spread(plant_info):
    plant_info.get_url_info()

    # Retrieve the plant spread
    plant_spread = plant_info.get_spread()

    # Assert that the plant spread is not None (indicating it was found)
    assert plant_spread is not None, "Plant spread should not be None"

    # Assert specific expected values if known
    expected_plant_spread = "2m"
    assert plant_spread == expected_plant_spread, f"Expected plant spread '{expected_plant_spread}', got '{plant_spread}'"

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
