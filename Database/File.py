import pandas as pd

class File:
    user_input_csv = None
    
    def __init__(self, user_input_csv: str):
        self.user_input_csv = user_input_csv
    
    def get_test_function_data(self):
        df = pd.read_csv(self.user_input_csv)
        data = list(df.itertuples(index=False, name=None))
        return data

    