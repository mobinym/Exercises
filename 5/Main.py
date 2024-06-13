from Extractions import * 
from Loads import *
from Transforms import *

### خواندن فایل csv
df = extract_csv('orders.csv')
# print(df)


###پاک کردن همه ستون های خالی 
drop_all_nan(df)
# print(df)

### پر کردن ستون های خالی 
fill_na(df)


### تغییر نوع داده ها به Int
change_data_type(df)

## one hot Encoder
df = one_hot_encoding(df)


## label encoding
label_encoding(df)


###پاک کردن ستون های بلااستفاده 
df=drop_columns(df,['CustomerName','PurchaseDate'])

###چک کردن داده های پرت در دو ستون 
# check_outlier(df,['PurchaseAmount','Weight'])


###پاک کردن داده های پرت 
df = remove_outlier(df,105000,280000)

###نرمالسازی 
df = min_max_scaling(df,['Product','Quantity','PurchaseAmount','Color','Weight','IsAvailable_No','IsAvailable_Yes'])

print(df)

###ذخیره در فایل 
load_csv(df,'target.csv')