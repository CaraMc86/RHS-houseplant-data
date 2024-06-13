import pytest
from get_plant_info import GetPlant

@pytest.fixture
def plant_info():
    # Setup necessary objects for the tests
    url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/'
    return GetPlant(url)

def test_get_about_info(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()
    instance.get_about_info()

    # Assert
    assert instance.about_list_items is not None, "about_list_items should not be None"
    assert len(instance.about_list_items) > 0, "about_list_items should contain items"

def test_get_position(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()  # This assumes you have a method to fetch URL content and parse it
    instance.get_about_info()
    position = instance._get_position()
    expected_position = 'Bright but indirect light'

    # Assert
    assert isinstance(position, str), "Position should be a string"
    assert position != 'N/A', "Position should not be 'N/A'"
    assert position.strip(), "Position should not be an empty string"
    assert position == expected_position

def test_get_soil(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()
    instance.get_about_info()
    soil = instance._get_soil()
    expected_soil = 'Peat free, general-purpose potting compost'

    # Assert
    assert isinstance(soil, str), "Soil should be a string"
    assert soil != 'N/A', "Soil should not be 'N/A'"
    assert soil.strip(), "Soil should not be an empty string"
    assert soil == expected_soil

def test_get_growthRate(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()
    instance.get_about_info()
    growth_rate = instance._get_growthRate()
    expected_growth_rate = 'Average to fast'

    # Assert
    assert isinstance(growth_rate, str), "Growth rate should be a string"
    assert growth_rate != 'N/A', "Growth rate should not be 'N/A'"
    assert growth_rate.strip(), "Growth rate should not be an empty string"
    assert growth_rate == expected_growth_rate

def test_get_homeCare(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()
    instance.get_about_info()
    home_care = instance._get_homeCare()
    expected_home_care = 'Keep it out of direct sunlight, ideally in a bright spot, and mist the leaves, particularly if the room is warm and dry. Also the leaves will appreciate being given a wash sometimes to keep them clean and dust free. This plant likes a moist soil but not a waterlogged soil, so in the winter feel the soil before you water it. In the summer you can water more freely.'

    # Assert
    assert isinstance(home_care, str), "Home care should be a string"
    assert home_care != 'N/A', "Home care should not be 'N/A'"
    assert home_care.strip(), "Home care should not be an empty string"
    assert home_care == expected_home_care

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
