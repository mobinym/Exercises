import pandas as pd   
def Extractfile_csv(filepath):
    df=pd.read_csv(filepath)
    return df