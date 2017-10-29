from twilio.rest import Client
import os
from settings import TWILIO_NUMBER, AUTH_TOKEN, ACCOUNT_SID, LINDSAY
# Your Account SID from twilio.com/console
account_sid = ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token  = AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=LINDSAY,
    from_=TWILIO_NUMBER,
    body="Hello from Python!")

print(message.sid)
