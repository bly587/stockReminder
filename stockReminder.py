import os
from twilio.rest import Client
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from datetime import datetime
import pandas as pd
import numpy as np
from decouple import config


#START_DATE = '2021-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
START_DATE = END_DATE[:9] + "5"
#print(stuff)

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end= END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    #non null values
    return clean_data.fillna(method='ffill')

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', START_DATE, END_DATE)
        #print(stock_data)
        adj_close = clean_data(stock_data, 'Adj Close')
        return adj_close
    except RemoteDataError:
        print("No data found for {t}".format(t=ticker))

def get_change(data):
    #get newest data point
    newest = data[len(data) - 1]
    #print(newest)
    #recent oldest
    rec_old = data[len(data) - 2]
    #print(rec_old)
    #total change
    change = newest - rec_old
    change = (change / rec_old) * 100
    return change

# API_USERNAME = config('USER')
# API_KEY = config('KEY')
account_sid = config('SID')
print(account_sid)
# auth_token = os.environ[""]
# auth_token = ""
#
# client = Client(account_sid, auth_token)
#
# client.messages.create(
#     to="+18082061617",
#     from_="+12672637427",
#     body="This is a test"
# )


#get stock watchlist


i = get_data('TSLA')
print(i)
print(type(i))
print(len(i))
val = get_change(i)
#get price of stock and day change


#format text to user
#send text
