import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWAPI_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
parameter = {
    "lat": 10.543190,
    "lon":  76.136627,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alert"
}

response = requests.get(ENDPOINT, params=parameter)
weather_data = response.json()["weather"][0]["id"]

if weather_data < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = 'You need Umberla',
    from_='+12XXXXXXXXX',
    to='+91XXXXXXXXXX'
    )
    print(message.sid)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = 'You Dont need Umberla',
    from_='+12XXXXXXXXX',
    to='+91XXXXXXXXXX',
    )
    print(message.sid)