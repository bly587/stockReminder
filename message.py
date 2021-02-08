from twilio.rest import Client
from decouple import config


account_sid = config('SID')
auth_token = config("TOKEN")
phone = config("MY_PHONE")
robo = config("COMP_PHONE")

auth_token = ""

client = Client(account_sid, auth_token)

client.messages.create(
    to="",
    from_="",
    body="This is a test"
)


#get stock watchlist


i = get_data('TSLA')
print(i)
print(type(i))
print(len(i))
val = get_change(i)
#get price of stock and day change


#format text to user
#send text
