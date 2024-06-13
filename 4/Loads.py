import pandas as pd

def to_csv_daily_average(filepath,data):
    data.to_csv(filepath,index=True)

def to_csv_maxAmount_received_daily(filepath,data):
    data.to_csv(filepath,index=True)
def to_csv_minAmount_received_daily(filepath,data):
    data.to_csv(filepath,index=True)

def to_csv_traffic_times(filepath,data):
    data.to_csv(filepath,index=True)