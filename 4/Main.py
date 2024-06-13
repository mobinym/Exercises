from Extractions import *
from Loads import *
from Transforms import *



data = Extractfile_csv('report.csv')

###مقداری وجود نداشت 
# data = drop_all_na(data)
# print(data)


#پاک کردن ستون های بلااستفاده در تحلیل
drop_useless_columns(data,['Customer_Name','Customer_email','mobile_number','Name_cashier','Price_Product','Transportation_fare','amount_discount'])
# print(data)

###تبدیل تاریخ به عدد 
# LabelEncoding(data,['date_time'])
# print(data)

###تبدیل به عدد کردن مبالغ پرداخت شده
data = change_data_type(data)
# print(data)


#--------میانگین روزانه------------------
daily_average=daily_avg(data)
#حداقل مبلغ خرید در روز
min_amount=min_amount_received(data)
#حداکثر مبلغ خرید در روز
max_amount=max_amount_received(data)
#ترافیک روزانه 
traffic_daily = traffic_times(data)



#--------------ذخیره تحلیل های اماری---------------------
#--------------Analysis Data Folder-------------------------
print('\033[92m'+'Create file...'+'\033[0m')
to_csv_daily_average('Analysis Data/daily_avg.csv',daily_average)
to_csv_minAmount_received_daily('Analysis Data/min_amount_received.csv',min_amount)
to_csv_maxAmount_received_daily('Analysis Data/max_amount_received.csv',max_amount)
to_csv_traffic_times('Analysis Data/traffic_times.csv',traffic_daily)
print('\033[92mDone...\033[0m')