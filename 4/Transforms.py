import pandas as pd

def drop_all_na(data):
    #درصورت بودن رکوردی که کل سطر خالی باشه 
    data.dropna(how='all',axis= 0 ,inplace=True)
    return data


def find_duplicates(data,columns):
    #پیدا کردن مقادیر تکراری 
    duplicates = data.duplicated(subset=columns,keep=False)
    show_duplicated = data[duplicates]
    sort = show_duplicated.sort_values(by=columns)
    return sort

def drop_useless_columns(data,columns):
    #پاک کردن ستون هایی که در تحلیل نیازی نداشتیم بهش
    for col in columns:
        data.drop(col,axis=1,inplace=True)
    return data


#برای تاریخ 
from sklearn.preprocessing import LabelEncoder
def LabelEncoding(data, columns):
    le = LabelEncoder()
    for column in columns:
        data[column] = le.fit_transform(data[column])
    return data

#تبدیل به عدد کردن مبالغ پرداخت شده 
def change_data_type(df):
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['Amount_received'] = df['Amount_received'].str.replace('$', '').astype(float)
    return df

def daily_avg(df):
    # میانگین خرید روزانه
    dailyavg = df.groupby(df['date_time'].dt.date)['Amount_received'].mean()
    return dailyavg

def min_amount_received(df):
    # حداقل مبلغ خرید در روز
    daily_min = df.groupby(df['date_time'].dt.date)['Amount_received'].min()
    return daily_min
    
def max_amount_received(df):
    # حداکثر مبلغ خرید در روز
    daily_max = df.groupby(df['date_time'].dt.date)['Amount_received'].max()
    return daily_max

def traffic_times(df): 
    # زمان‌های پرترافیک خرید
    traffic_days = df.groupby(df['date_time'].dt.date).size()
    return traffic_days
