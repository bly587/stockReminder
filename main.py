from stockValue import get_values
from message import updateMessage

#main file
#use stockValue to get values of each company
#use message.py to send values to user
#get stock watchlist
filename = "watchlist.txt"
with open(filename) as f:
    content = f.readlines()

#get day change of each stock on watchlist and store in dictionary
info = get_values(content)

#send message
updateMessage(info)
