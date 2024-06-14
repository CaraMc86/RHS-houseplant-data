# In test_database.py

import pytest
import sqlite3 as sql
from database import PlantDatabase


@pytest.fixture(scope="module")
def db_connection():
    # Connect to an in-memory SQLite database for testing
    conn = sql.connect(':memory:')
    yield conn
    conn.close()


def test_create_table(db_connection):
    # Initialize PlantDatabase instance with the fixture connection
    plant_db = PlantDatabase()
    plant_db.connect()

    # Call the method to create the 'plants' table
    plant_db.createHouseplantTable()

    # Assertions or further tests to validate table creation can be added here

    # Close the connection after testing
    plant_db.closeConnection()


def test_drop_table(db_connection):
    # Initialize PlantDatabase instance with the fixture connection
    plant_db = PlantDatabase()
    plant_db.connect()

    # Call the method to drop the 'plants' table
    plant_db.dropTable()

    # Assertions or further tests to validate table drop can be added here

    # Close the connection after testing
    plant_db.closeConnection()


def test_connect_and_close_connection(db_connection):
    # Initialize PlantDatabase instance with the fixture connection
    plant_db = PlantDatabase()

    # Call the connect method to establish a connection
    plant_db.connect()

    # Assertions or further tests to validate connection establishment can be added here

    # Call the closeConnection method to close the connection
    plant_db.closeConnection()

