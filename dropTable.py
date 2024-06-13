from plantsConnect import *

try:
    # Drop the "plants" table if it exists
    db_cursor.execute("DROP TABLE IF EXISTS plants")
    db_con.commit()
    print("Table 'plants' dropped successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    db_con.close()