import pandas as pd

###پاک کردن همه سطرهای خالی
def drop_all_nan(data):
    data.dropna(how='all', inplace=True)
    return data

### پر کردن هر ستون با mean & mode
def fill_na(data):
    data['PurchaseAmount'] = pd.to_numeric(data['PurchaseAmount'], errors='coerce')
    data.fillna(value={
        'PurchaseDate':data.PurchaseDate.mode()[0],
        'Product':data.Product.mode()[0],
        'Quantity':data.Quantity.mean(),
        'PurchaseAmount':data.PurchaseAmount.mean(),
        'Color':data.Color.mode()[0],
        'IsAvailable':data.IsAvailable.mode()[0],
        'Weight':data.Weight.mean()
    }
    , inplace=True
    )
    return data

### تغییر نوع داده ای ستون ها به عدد 
def change_data_type(data):
    data.Weight = round(data.Weight, 2)
    data.Quantity = round(data.Quantity).astype('int')
    data.PurchaseAmount = round(data.PurchaseAmount).astype('int')
    return data

## one hot Encoder
def one_hot_encoding(data):
    data = pd.get_dummies(data, columns=['IsAvailable'])
    data = data.astype({'IsAvailable_No':'int', 'IsAvailable_Yes':'int'})
    return data

### پاک کردن ستون هایی که نیاز نداریم 
def drop_columns(data,columns):
    for col in columns:
        data.drop(col, axis=1, inplace=True)
    return data


## label encoding
from sklearn.preprocessing import LabelEncoder
def label_encoding(data):
    label_encoder = LabelEncoder()
    data['Product'] = label_encoder.fit_transform(data['Product'])  
    data['Color'] = label_encoder.fit_transform(data['Color'])
    return data



###پیدا کردن داده های پرت با رسم نمودار 
import plotly.express as px
def check_outlier(data,columns):
    fig = px.box(data, y=columns)
    fig.show()

### پاک کردن داده های پرت
def remove_outlier(data,minPurchase,maxPurchase):
    df= pd.DataFrame(data)
    data = df[(df['PurchaseAmount']>=minPurchase) & (df['PurchaseAmount']<=maxPurchase)]
    return data


### نرمال سازی
from sklearn.preprocessing import MinMaxScaler
def min_max_scaling(data,columns):
    scaler = MinMaxScaler()
    data= scaler.fit_transform(data)
    data= pd.DataFrame(data)
    data.columns = columns
    return data
