from twilio.rest import Client
from decouple import config


account_sid = config('SID')
auth_token = config("TOKEN")
phone = config("MY_PHONE")
robo = config("COMP_PHONE")


client = Client(account_sid, auth_token)

def updateMessage(msg):
    client.messages.create(
        to=phone,
        from_=robo,
        body=msg
    )

# client.messages.create(
#     to="",
#     from_="",
#     body="This is a test"
# )
