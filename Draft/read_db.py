# import sqlite3
# import pandas as pd

# connection = sqlite3.connect('list_test_function.db')
# cursor = connection.cursor()

# def get_test_function_data():
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv('test_function_db.csv')
#     # Convert DataFrame to list of tuples
#     data = list(df.itertuples(index=False, name=None))
#     return data

# def read_data_from_db():
#     global connection, cursor
#     cursor.execute('SELECT * FROM evaluation_test_cases')
#     rows = cursor.fetchall()
#     return rows

# def show_data():
#     data = read_data_from_db()
#     for row in data:
#         print(row)

# def insert_data(data):
#     global connection, cursor
#     cursor.executemany('INSERT INTO evaluation_test_cases (function, input, output) VALUES (?, ?, ?)', data)
#     connection.commit()
    
# def create_table():
#     global connection, cursor
#     cursor.execute('DROP TABLE IF EXISTS evaluation_test_cases')
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS evaluation_test_cases (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         function TEXT NOT NULL,
#         input TEXT NOT NULL,
#         output TEXT NOT NULL
#     )
#     ''')
#     connection.commit()
   

# if __name__ == '__main__':
#     create_table()
#     data = get_test_function_data()
#     insert_data(data)
#     show_data()
#     connection.close()