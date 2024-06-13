from datetime import datetime,date
from khayyam import *


getdate = input('Enter Date (For Example: 1399-06-20):')
splitdate = getdate.split('-')
getyear=int(splitdate[0])
getmonth=int(splitdate[1])
getday=int(splitdate[2])


d1 = JalaliDate(getyear,getmonth,getday)
d2 = (d1.todate())
d3 = date.today()
d4day = abs(d2-d3).total_seconds()/(60*60*24)

print(f'Time difference is : {d4day} day')