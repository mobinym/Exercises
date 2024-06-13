import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Analysis Data/daily_avg.csv')
x = data['date_time']
y = data['Amount_received']
plt.subplot(2,2,1)
plt.bar(x,y,color='blue')

plt.title('daily_avg')
plt.xlabel('Date')
plt.ylabel('Amount Received')
#---------------------------------------------------------------
data = pd.read_csv('Analysis Data/max_amount_received.csv')
x = data['date_time']
y = data['Amount_received']
plt.subplot(2,2,2)
plt.bar(x,y,color='green')
plt.title('max_amount_received')
plt.xlabel('Date')
plt.ylabel('Amount Received')
#---------------------------------------------------------------
data = pd.read_csv('Analysis Data/min_amount_received.csv')
x = data['date_time']
y = data['Amount_received']
plt.subplot(2,2,3)
plt.bar(x,y,color='black')
plt.title('min_amount_received')
plt.xlabel('Date')
plt.ylabel('Amount Received')
#---------------------------------------------------------------
data = pd.read_csv('Analysis Data/traffic_times.csv')
x = data['date_time']
y = data['0']
plt.subplot(2,2,4)
plt.bar(x,y,color='red')
plt.title('traffic_times')
plt.xlabel('Date')
plt.ylabel('Amount Received')

plt.show()