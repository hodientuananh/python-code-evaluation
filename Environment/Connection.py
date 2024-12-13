import sqlite3

from Environment.const import EVALUATION_TEST_DB

class Connection:
    connection = None
    cursor = None
    
    def __init__(self):
        self.connection = sqlite3.connect(EVALUATION_TEST_DB)
        self.cursor = self.connection.cursor()
        
    def get_connection(self):
        return self.connection
    
    def get_cursor(self):
        return self.cursor
    