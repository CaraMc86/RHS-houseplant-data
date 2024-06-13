import pytest
from get_plant_info import GetPlant

# Define a fixture to instantiate GetPlant with the URL
@pytest.fixture
def plant_info():
    url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/'
    return GetPlant(url)

# Test case to fetch and validate the plant name
def test_get_plant_name(plant_info):
    # Fetch HTML content and parse with BeautifulSoup
    plant_info.get_url_info()

    # Retrieve the plant name
    plant_name = plant_info.get_plant_name()

    # Assert that the plant name is not None (indicating it was found)
    assert plant_name is not None, "Plant name should not be None"

    # Assert specific expected values if known
    expected_plant_name = "Monstera deliciosa"
    assert plant_name == expected_plant_name, f"Expected plant name '{expected_plant_name}', got '{plant_name}'"
# Test case to fetch and validate the alternative plant name
def test_get_alt_plant_name(plant_info):
    # Fetch HTML content and parse with BeautifulSoup
    plant_info.get_url_info()

    # Retrieve the alternative plant name
    alt_name = plant_info.get_alt_plant_name()

    # Assert that the alternative plant name is not None (indicating it was found)
    assert alt_name is not None, "Alternative plant name should not be None"

    # Assert specific expected values if known
    expected_alt_name = "Swiss cheese plant ( syn. Monstera pertusum )"
    assert alt_name == expected_alt_name, f"Expected alternative name '{expected_alt_name}', got '{alt_name}'"

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()

