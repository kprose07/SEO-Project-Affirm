import os
from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACe94b55d99efc7e695808cb2ad3f43786'
auth_token = '24c0cc3ccdb67b6a53da291b8b4e7cc6'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+18556200235',
         to='+18034766717'
     )

print(message.sid)