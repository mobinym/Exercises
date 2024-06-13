import requests
from bs4 import BeautifulSoup
import json


url = requests.get('https://www.entekhabcenter.com/product-category/product/audio-video/television')
# print(url.status_code)

soup = BeautifulSoup(url.content,'html.parser')
#------------NAME----------------------------
namelist = [] 
names = soup.find_all('h5')
for i in names:
    namelist.append(i.text)

#-------------Price----------------------
pricelist = []
prices = soup.select('ins>b')
for i in prices:
    pricelist.append(i.text)
#---------------Item List---------------------
item= []
zip1 =  zip(namelist,pricelist)
for name,price in zip1:
    item.append({'Name' : name , 'Price' : price})

#-------------------------------------------
try:
    #استفاده از utf-8 برای متن فارسی
    with open('Homework 9/practice2/F1.json' , 'w',encoding='utf-8') as file1:
        # ensure_ascii = false => for write persian sentences
        json.dump(item,file1,ensure_ascii=False,indent=4)

except Exception as error:
    print('\033[31m'+str(error)+'\033[0m')

else:
    print('\033[32m'+'Done F1.json Created ...'+'\033[0m')