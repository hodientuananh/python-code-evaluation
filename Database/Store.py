from Database.File import File
import Environment.Connection as Connection

class Store:
    db_name = None
    table_name = None
    file = None
    conn = None
    
    def __init__(self, db_name: str, table_name: str, file: File, conn: Connection):
        self.db_name = db_name
        self.table_name = table_name
        self.file = file
        self.conn = conn
        
        self._init_data()
        
    def _init_data(self):
        self.__create_table()
        self.__insert_data()

    def __create_table(self):
        drop_query = f'DROP TABLE IF EXISTS {self.table_name}'
        create_query = f'''
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_function TEXT NOT NULL,
            function TEXT NOT NULL,
            input TEXT NOT NULL,
            output TEXT NOT NULL
        )
        '''
        connection = self.conn.get_connection()
        cursor = self.conn.get_cursor()
        cursor.execute(drop_query)
        cursor.execute(create_query)
        connection.commit()
    
    def get_data_from_db(self):
        query = f'SELECT * FROM {self.table_name}'
        cursor = self.conn.get_cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
        
    def is_table_exist(self):
        query = f'SELECT name FROM sqlite_master WHERE type="table" AND name="{self.table_name}"'
        cursor = self.conn.get_cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        return row is not None
        
    def __insert_data(self):
        data = self.file.get_test_function_data()
        if not data:
            return
        if not self.is_table_exist():
            self.create_table()
        query = f'INSERT INTO {self.table_name} (test_function, function, input, output) VALUES (?, ?, ?, ?)'
        connection = self.conn.get_connection()
        cursor = self.conn.get_cursor()
        cursor.executemany(query, data)
        connection.commit()
