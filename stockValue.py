from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from datetime import datetime
import pandas as pd
import numpy as np


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
    change = str(round(change, 2))
    return [change, str(round(newest, 2))]

def formatDict(dict):
    str = "S: P: %"
    for key in dict.keys():
        str += "\n" + key[:len(key) - 1] + ": " +dict.get(key)[1]+ ": " +dict.get(key)[0] +"%"
    #print(str)
    return str

def get_values(tickers):
    stockDict = {}
    for value in tickers:
        #get %change and current price
        i = get_change(get_data(value[:len(value) - 1]))
        stockDict[value] = i
    final = formatDict(stockDict)
    return final



# #get stock watchlist
# filename = "watchlist.txt"
# with open(filename) as f:
#     content = f.readlines()
#
# #get day change of each stock on watchlist and store in dictionary
# info = get_values(content)
#
# formatDict(info)
