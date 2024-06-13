import pandas as pd


def drop_record_all_nans(df):
    return df.dropna(how = 'all',axis = 0)
#-------------------------------------------------
def fillna(df):
    df['daily_patients']=pd.to_numeric(df['daily_patients'],errors='coerce')
    df['treated_patients']=pd.to_numeric(df['treated_patients'],errors='coerce')
    df['discharged_patients']=pd.to_numeric(df['discharged_patients'],errors='coerce')
    df['deaths']=pd.to_numeric(df['deaths'],errors='coerce')
    df.fillna(value={
        'daily_patients':df['daily_patients'].mean(),
        'treated_patients':df['treated_patients'].mean(), 
        'discharged_patients':df['discharged_patients'].mean(), 
        'deaths':df['deaths'].mean()
        },inplace=True
    )
    return df
#------------------------------------------------------------------------------

def show_duplicated(df):
    df_duplicate_record = df.duplicated(subset=['hospital_name','daily_patients','treated_patients','discharged_patients','deaths'],keep=False)
    duplicate_records = df[df_duplicate_record]
    sort =  duplicate_records.sort_values(by=['hospital_name','daily_patients'])
    return sort

#-----------------------------------------------------------------------------------
def drop_duplicated(df):
    df_drop_duplicate = df.drop_duplicates(subset=['hospital_name','daily_patients','treated_patients','discharged_patients','deaths'],keep='first',inplace=True)
    return df_drop_duplicate

# ----------------------------------------------------------

def change_data_type(df):
    df=df.astype({'daily_patients':'int'})
    df=df.astype({'treated_patients':'int'})
    df=df.astype({'discharged_patients':'int'})
    df=df.astype({'deaths':'int'})
    return df
# ----------------------------------------------------------
import plotly.express as px
def check_outliers_data(data,columns):
    fig = px.box(data, y=columns)
    fig.show()
# ----------------------------------------------------------
