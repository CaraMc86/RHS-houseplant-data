import sqlite3 as sql # import the sqlite3 module and give it the alias 'sql'

try:
    # to use the sqlite module we start by creating a db connection object(variable to hold the folder path with the filename)
    with sql.connect('C:/Python/JUST-IT/Web Scraping/plant_care.db') as db_con:
        # Once the db file create a cursor object and bind it to the cursor method from the sqlite module.
        db_cursor = db_con.cursor()
except sql.OperationalError as oe: #Raise a sql error as oe (operational error)
    # Handle the error with a message
    print(f'Connection failed: {oe}')





