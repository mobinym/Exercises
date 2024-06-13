import pandas as pd 

def read_csv(filepath):
    data = pd.read_csv(filepath)
    return data