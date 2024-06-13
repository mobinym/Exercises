import numpy as np 
import pandas as pd 
 
data = pd.read_csv('data2.csv')
# print(data)
# print(data.columns)

def fill_na(data):
    data.fillna(data['December income'].mean(), inplace=True)
fill_na(data)


def drop_columns(data):
    data.drop(['Age','Height','Weight','Gender','Hobby','City','Education','MaritalStatus','Number of children'], axis=1, inplace=True)
drop_columns(data)


namelist = []
for i in data['Name']:
    namelist.append(i)
# print(namelist)

average =  data.drop('Name', axis=1).mean(axis=1)
averagelist = []
for i in average.round(2):
    averagelist.append(i)
# print(averagelist)


data2 = pd.DataFrame({
    'Name': namelist,
    'Average': averagelist
    })
print(data2)

#--------------------------FIRST CHART------------------------------------------

import matplotlib.pyplot as plt
#Average income chart


Name = namelist
average = averagelist
plt.subplot(1,2,1) 
plt.bar(Name, average, color='blue')
plt.xlabel('Name', fontsize=14, fontweight='bold',labelpad=10, color='red')
plt.ylabel('Average', fontsize=14, fontweight='bold',labelpad=10,color='red')
plt.title('Average of all the data',fontsize=14, fontweight='bold', color='green')

#---------------------------SECOND CHART-------------------------------------------
#Chart of income in 12 months for each person
data.set_index('Name', inplace=True)
plt.subplot(1,2,2)
for name in data.index:
    plt.plot(data.columns, data.loc[name], label=name , linestyle='-')

plt.xlabel('Month', fontsize=14, fontweight='bold',labelpad=10, color='red')
plt.ylabel('Income', fontsize=14, fontweight='bold',labelpad=10, color='red')
plt.title('Income trend in 12 months', fontsize=14, fontweight='bold', color='green')
#for better display the months in the chart
plt.xticks(rotation=30)

plt.legend()

####برای نمایش بهتر بعد از اجرا شدن در تنظیمات جدول مقدار BOTTOM را زیاد کنید 
plt.show()