import sqlite3

connection = sqlite3.connect('list_test_function.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS evaluation_test_cases')
cursor.execute('''
CREATE TABLE IF NOT EXISTS evaluation_test_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    function TEXT NOT NULL,
    input TEXT NOT NULL,
    output TEXT NOT NULL,
)
''')

cursor.executemany('INSERT INTO evaluation_test_cases (function, input, output) VALUES (?, ?, ?)', [
    
])

connection.commit()

cursor.execute('SELECT * FROM evaluation_test_cases')
rows = cursor.fetchall()  # Fetch all results
for row in rows:
    print(row)
connection.close()