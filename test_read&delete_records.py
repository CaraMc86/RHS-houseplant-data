import pytest
import sqlite3 as sql
from database import PlantDatabase

@pytest.fixture(scope="module")
def db_connection():
    conn = sql.connect(':memory:')
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def setup_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS housePlants (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            plantName TEXT,
            altName TEXT,
            eventualHeight TEXT,
            eventualSpread TEXT,
            position TEXT,
            soil TEXT,
            growthRate TEXT,
            hardiness TEXT,
            homeCare TEXT,
            hazards TEXT
        )
    """)
    db_connection.commit()
    yield
    cursor.execute("DROP TABLE IF EXISTS housePlants")
    db_connection.commit()

def test_create_table(db_connection):
    plant_db = PlantDatabase()
    plant_db.conn = db_connection
    plant_db.cursor = db_connection.cursor()
    plant_db.createHouseplantTable()
    assert True

def test_connect_and_close_connection(db_connection):
    plant_db = PlantDatabase(':memory:')
    plant_db.connect()
    assert plant_db.conn is not None
    plant_db.closeConnection()
    assert plant_db.conn is None

def test_read_records(db_connection):
    plant_db = PlantDatabase()
    plant_db.conn = db_connection
    plant_db.cursor = db_connection.cursor()
    plant_db.cursor.execute("""
        INSERT INTO housePlants (plantName, altName, eventualHeight, eventualSpread, position, soil, growthRate, hardiness, homeCare, hazards)
        VALUES ('Another Test Plant', 'Another Alt', '2m', '2m', 'Shade', 'Clay', 'Slow', 'Tender', 'Moderate', 'Toxic')
    """)
    plant_db.conn.commit()
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    plant_db.readRecords('housePlants')
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert 'Another Test Plant' in output

    captured_output = io.StringIO()
    sys.stdout = captured_output
    plant_db.readRecords('nonExistingTable')
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert 'Table \'nonExistingTable\' doesn\'t exist' in output

def test_delete_record(db_connection):
    plant_db = PlantDatabase()
    plant_db.conn = db_connection
    plant_db.cursor = db_connection.cursor()
    plant_db.cursor.execute("""
        INSERT INTO housePlants (plantName, altName, eventualHeight, eventualSpread, position, soil, growthRate, hardiness, homeCare, hazards)
        VALUES ('Test Plant', 'Test Alt', '1m', 
