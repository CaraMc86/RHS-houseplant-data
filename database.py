import sqlite3 as sql

class PlantDatabase:

    def __init__(self, db_file='plants.db'):
        """Initialise the attributes needed for database creation and management"""
        # Initialises the database file name, calling it plants.db as default as above, unless otherwise specified
        # This also stores the file path to be used in the other methods, so it does not have to be explicitly written out, allowing it to be reused.
        self.db_file = db_file
        # Initialises an empty connection object. This will be assigned a value when connecting to the database - in the methods underneath.
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            if self.db_file == ':memory:':
                self.conn = sql.connect(':memory:')
            else:
                self.conn = sql.connect(self.db_file)
            self.cursor = self.conn.cursor() # """*******************remove if else block when all tests are complete*********************"""
            # # assign the previously empty db_conn object with a connection to the db_file using sql connect
            # # As db_file stores the pth when created, the full file path is not required
            # self.conn = sql.connect(self.db_file)
        except sql.OperationalError as oe:  # Raise a sql error as oe (operational error)
            # Handle the error with a message
            print(f'Connection failed: {oe}')

    def closeConnection(self):
        try:
            if self.conn:
                # If self.conn is not None (so a connection exits), the .close() method will close the database.
                self.conn.close()
                self.conn = None
                print('Database connection closed')
        except sql.OperationalError as oe:
            # Handle the error with a message
            print(f'Connection closure failed: {oe}')

    def tableExists(self, table_name):
        if self.conn is None or self.cursor is None:
            raise RuntimeError("Database connection is not established.")
        try:
            self.cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=?', (table_name,))
            table_exists = self.cursor.fetchone()
            return table_exists is not None
        except sql.Error as e:
            print(f"An error occurred: {e}")
            return False
    def createHouseplantTable(self):
        if self.conn is None or self.cursor is None:
            raise RuntimeError("Database connection is not established.")

        create_table_sql = """
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
                """
        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            if self.cursor.lastrowid:
                print('Table \'housePlants\' created successfully')
            else:
                print('Table already exists')
        except sql.Error as e:
            print(f"Error creating 'plants' table: {e}")



    def readRecords(self, table_name):
        if self.conn is None or self.cursor is None:
            raise RuntimeError("Database connection is not established.")
        if not self.tableExists(table_name):
            print(f'Table \'{table_name}\' doesn\'t exist')
            return
        try:
            self.cursor.execute(f'SELECT * FROM {table_name}')
            records = self.cursor.fetchall()
            for record in records:
                print(record)
        except sql.Error as e:
            print(f"An error occurred: {e}")



    def deleteRecord (self, table_name, id_field):
        """Function defined taking the id_field as a parameter to allow a specific ID to be called and a record deleted."""
        if self.conn is None or self.cursor is None:
            raise RuntimeError("Database connection is not established.")
        if not self.tableExists(table_name):
            print(f'Table \'{table_name}\' doesn\'t exist')
            return
        try:
            self.cursor.execute('DELETE FROM housePlants WHERE ID = ?', (id_field,))
            self.conn.commit()
            print(f'Song with ID {id_field} deleted successfully')
        except sql.ProgrammingError as pe:  # Use to handle invalid SQL statement
            print(f"Failed operation: {pe}")

    def dropTable(self):
        if self.conn is None or self.cursor is None:
            raise RuntimeError("Database connection is not established.")

        try:
            # Drop the "housePlants" table if it exists
            self.cursor.execute("DROP TABLE IF EXISTS housePlants")
            self.conn.commit()
            print("Table 'housePlants' dropped successfully.")
        except sql.Error as e:
            print(f"An error occurred: {e}")
