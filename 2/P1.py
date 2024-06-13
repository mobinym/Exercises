import pandas as pd
import numpy as np 

#-----------READ CSV-----------------------------------------------------
data = pd.read_csv('data.csv')

#-----------DELETE 'SARA'  -----------------------------------------------
def delete_wrong_data(data):
    data.drop(data[data['Name'] == 'Sara'].index, inplace=True)

delete_wrong_data(data)

#-----------CHANGE WRONG TYPE---------------------------------------------
def Change_Str_To_Nan(data):
    data['Weight'] = pd.to_numeric(data['Weight'], errors='coerce')
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

Change_Str_To_Nan(data)

#-----------FILL NAN------------------------------------------------------
def fill_na(data):
    data.fillna(value={
     'Weight': data['Weight'].mean(),
     'Age': int(data['Age'].mean()),
     'Gender':data['Gender'].mode()[0],
     'Hobby':data['Hobby'].mode()[0],
     'Education':data['Education'].mode()[0],
     'MaritalStatus':data['MaritalStatus'].mode()[0]

     },inplace=True)

fill_na(data)

#-----------CHANGE TYPE TO 'INT'---------------------------------------------
def astype(df):
    df['Age'] = df['Age'].astype(int)
    df['Weight'] = df['Weight'].astype(int)

astype(data)

#-----------MEAN-------------------------------------------------------------
def Age_Weight_Mean(data):
    print(f'Age mean is : {data.Age.mean()}')
    print(f'Weight mean is : {data.Weight.mean()}')
    print(100*'-')

#-----------MEDIAN-----------------------------------------------------------
def Age_Weight_Median(data):
    print(f'Age median is : {data.Age.median()}')
    print(f'Weight median is : {data.Weight.median()}')
    print(100*'-')

#-----------MODE------------------------------------------------------------
def Mode_Data(data):
    print(f'Height mode is : {data.Height.mode()[0]}')
    print(f'Gender mode is : {data.Gender.mode()[0]}')
    print(f'Education mode is : {data.Education.mode()[0]}')
    print(100*'-')

#-----------RANGE-----------------------------------------------------------
def range_data(data):
    print(f'Age Range is: {np.ptp(data['Age'])}')
    print(f'Height Range is: {np.ptp(data['Height'])}')
    print(f'Weight Range is: {np.ptp(data['Weight'])}')
    print(100*'-')

#-----------VARIENCE------------------------------------------------------
def Varience_Value(data):
    print(f'Age Varience is: {np.var(data['Age'])}')
    print(f'Height Varience is: {np.var(data['Height'])}')
    print(f'Weight Varience is: {np.var(data['Weight'])}')
    print(100*'-')

#-----------STANDART_DEVIATION--------------------------------------------
def Std_Deviation_value(data):
    print(f'Age STD is: {np.std(data['Age'])}')
    print(f'Height STD is: {np.std(data['Height'])}')
    print(f'Weight STD is: {np.std(data['Weight'])}')
    print(100*'-')

#-----------Quartiles-----------------------------------------------------
def Quartiles(data):
    print(f'Age Quartiles is: {np.percentile(data['Age'],[25,50,75])}')
    print(f'Height Quartiles is: {np.percentile(data['Height'],[25,50,75])}')
    print(f'Weight Quartiles is: {np.percentile(data['Weight'],[25,50,75])}')
    print(100*'-')

#-----------IQR----------------------------------------------------------
def IQR(data):
    Age_Q1 = np.percentile(data['Age'],25)
    Age_Q2 = np.percentile(data['Age'],75)
    Age_IQR = Age_Q2 - Age_Q1
    print(f'Age IQR is: {Age_IQR}')
    #--------------------------------------------------------------------
    Height_Q1 = np.percentile(data['Height'],25)
    Height_Q2 = np.percentile(data['Height'],75)
    Height_IQR = Height_Q2 - Height_Q1
    print(f'Height IQR is: {Height_IQR}')
    #-------------------------------------------------------------------
    Weight_Q1 = np.percentile(data['Weight'],25)
    Weight_Q2 = np.percentile(data['Weight'],75)
    Weight_IQR = Weight_Q2 - Weight_Q1
    print(f'Weight IQR is: {Weight_IQR}')
    print(100*'-')

#----------------MAIN-------------------------------------
Age_Weight_Mean(data)
Age_Weight_Median(data)
Mode_Data(data)
range_data(data)
Varience_Value(data)
Std_Deviation_value(data)
Quartiles(data)
IQR(data)


