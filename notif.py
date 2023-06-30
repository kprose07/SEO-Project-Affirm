import os
from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_notification(message):    
    account_sid = os.environ['TWIL_SID']
    auth_token = os.environ['TWILIO_API_KEY']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body= message,
            from_='+18556200235',
            to='+18034766717'
        )
    return message.sid
    print(message.sid)