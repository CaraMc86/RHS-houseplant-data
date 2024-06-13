from plantsConnect import *

# Create the "plants" table
db_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS plants (
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
    """
)

# Commit the changes
db_con.commit()

# Confirm table creation or display a message to confirm the table already exists
if db_cursor.lastrowid:
    print("Table 'plants' created successfully.")
else:
    print("Table 'plants' already exists.")

# Close the connection
db_con.close()