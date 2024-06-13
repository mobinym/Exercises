import jmespath
import json

with open('Homework 8/employee.json','r') as file1:
    data = json.load(file1)

#-------------------------------------------------------------------------
print('Names & family of female employees in all companies...')
print(jmespath.search("[?gender==`female`].fullName",data))
print(100*'-')
#-------------------------------------------------------------------------
print('Names & family male employees of MANPA company...')
print(jmespath.search("[?company==`MAPNA` && gender==`male`].fullName",data))
print(100*'-')
#-------------------------------------------------------------------------
print('Names & Family & e-mails of employees of Iran Khodro Co....')
print(jmespath.search("[?company==`Iran Khodro Co.`].[fullName,email]",data))
print(100*'-')
#-------------------------------------------------------------------------
print('top_3_male_employees...')
salary = [employee for employee in data if employee['gender']=='male']
salary.sort(key=lambda x: x['salary'],reverse=True)
sort_salary = salary[:3]
for i in sort_salary:
    print(i)
print(100*'-')
#-------------------------------------------------------------------------

