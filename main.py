from Database.File import File
from Database.Store import Store
from Environment.Connection import Connection
from Environment.const import EVALUATION_TABLE_NAME, EVALUATION_TEST_DB, EVALUATION_USER_INPUT_CSV

if __name__ == '__main__':
    db_name = EVALUATION_TEST_DB
    table_name = EVALUATION_TABLE_NAME
    user_input_csv = EVALUATION_USER_INPUT_CSV
    file = File(user_input_csv=user_input_csv)
    conn = Connection()
    
    store = Store(db_name=db_name, table_name=table_name, file=file, conn=conn)
    rows = store.get_data_from_db()
    print(rows)