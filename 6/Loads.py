import pandas as pd
def loadsdata(data,filepath):
    data.to_csv(filepath,index=False)

    