from plantsConnect import *

try:
    # Delete all rows from the "plants" table
    db_cursor.execute("DELETE FROM plants")

    # Reset the auto-increment counter for the table (optional)
    db_cursor.execute("DELETE FROM sqlite_sequence WHERE name='plants'")

    db_con.commit()
    print("Table 'plants' truncated successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    db_con.close()