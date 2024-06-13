import pandas as pd

def load_csv(data,filepath):
    data.to_csv(filepath, index=False)