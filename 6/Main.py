from Extraction import * 
from Loads import * 
from Transforms import * 



def display_data(data):
    print(80*'-')
    print(data)
    print(80*'-')

data = read_csv('hospital.csv')
# display_data(data.head())
#-------------------پاک کردن رکورد ها با مقادیر کاملا خالی-------------------------------

# print('\033[32mchecking data pls wait...\033[0m')
data = drop_record_all_nans(data)
# display_data(data.shape)
# print('\033[32mdone...\033[0m')

#---------------------تعداد تکراری ها -----------------------------

####25 duplicate noise
# print('\033[32mData Duplicates count...\033[0m')
# dup = data.duplicated(subset=['hospital_name', 'daily_patients', 'treated_patients',
#        'discharged_patients', 'deaths'],keep=False)
# display_data(dup.sum())
# print('\033[32mdone...\033[0m')

#-----------------------------تعداد مقادیر خالی------------------------------------

####29 null noise
# print('\033[32mData Nulls count...\033[0m')
# display_data(data.isnull().sum().sum())
# print('\033[32mdone...\033[0m')

#----------------------------------پر کردن مقادیر خالی-----------------------------------------

# print('\033[32mFill NaN...\033[0m')
data=fillna(data)
# display_data(data)
#----------------------------چک کردن برای عدم وجود مقدار خالی---------------------------------
# display_data(data.isnull().sum().sum())
# print('\033[32mdone...\033[0m')

#-------------------------------تعداد سطر و ستون مقادیر تکراری------------------------------------------------
# print('\033[32mDuplicate Data shape...\033[0m')
# display_data(show_duplicated(data).shape)
# print('\033[32mdone...\033[0m')


#-----------------تبدیل به عدد-----------------------
# print('\033[32mCHanging DataType...\033[0m')
data=change_data_type(data)
# display_data(data)
# print('\033[32mdone...\033[0m')


#-----------------پاک کردن مقادیر تکراری-------------------------
# print('\033[32mDrop Duplicate Data...\033[0m')
drop_duplicated(data)
# display_data(data)
# print('\033[32mdone...\033[0m')


#create file Target
loadsdata(data,'Target.csv')


### outliers data check 
# check_outliers_data(data,['daily_patients', 'treated_patients','discharged_patients', 'deaths'])
