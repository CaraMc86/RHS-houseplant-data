from plantsConnect import *
from new_plantV2 import *
import sqlite3


def add_plant_to_DB(plant_info):
    try:
        # Unpack the plant information tuple
        (plant_name, alt_name, eventual_spread, eventual_height, plant_position, soil_type, growth_rate, plant_hardiness, home_care, plant_hazard) = plant_info

        # Insert the data into the database - inset into with column names
        # Values with ? placeholder for each column
        db_cursor.execute('''
            INSERT INTO plants (plantName, altName, eventualHeight, eventualSpread, position, soil, growthRate, hardiness, homeCare, hazards)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (plant_name, alt_name, eventual_height, eventual_spread, plant_position, soil_type, growth_rate, plant_hardiness, home_care, plant_hazard))

        db_con.commit()
    except sqlite3.ProgrammingError as pe:
        print(f'Failed operation: {pe}')
    except sqlite3.OperationalError as oe:  # Raise a sql error as oe (operational error)
        # Handle the error with a message
        print(f'Connection failed: {oe}')
    except sqlite3.Error as e:  # Raise a sql error as oe (operational error)
        # Handle the error with a message
        print(f'Connection failed: {e}')


if __name__ == '__main__':
    plant_url = 'https://www.rhsplants.co.uk/plants/_/monstera-deliciosa/classid.2000032789/'
    plant_info = get_plant_info(plant_url)
    add_plant_to_DB(plant_info)