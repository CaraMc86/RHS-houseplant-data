import pytest
from get_plant_info import GetPlant

@pytest.fixture
def plant_info():
    # Setup necessary objects for the tests
    url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000048359/'
    return GetPlant(url)

def test_get_hazards_with_span(plant_info):
    # Setup
    instance = plant_info

    # Act
    instance.get_url_info()
    instance.get_hazards()
    expected_hazard = 'Humans/Pets: Harmful if eaten; skin/eye irritant'

    # Assert
    assert isinstance(instance.hazards, str) or instance.hazards is False, "Hazards should be a string or False"
    if isinstance(instance.hazards, str):
        assert instance.hazards.strip(), "Hazards should not be an empty string"
        assert instance.hazards == expected_hazard

# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
