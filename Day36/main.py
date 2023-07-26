import requests
import time
import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_MARKET_API = "xxxxxxxxxxxxxxxxxxxxx"
NEWS_API = "xxxxxxxxxxxxxxxxxxxxxxx"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxx"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_MARKET_API
}

news_params = {
    "q" : COMPANY_NAME,
    "apikey": NEWS_API
}

res = requests.get(STOCK_ENDPOINT, params=parameters)
stock_data = res.json()['Time Series (Daily)']
stock_list = [v for (k,v) in stock_data.items()]
yesterday_close = float(stock_list[0]['4. close'])
day_before_yesterday_close = float(stock_list[1]['4. close'])
difference = abs(yesterday_close - day_before_yesterday_close)
percentage = (difference / yesterday_close) * 100
if percentage > 1:
    print("get News")
    news_response  = requests.get(NEWS_ENDPOINT,params=news_params)
    news_data = news_response.json()['articles']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = f"""
    {percentage} Up
    Title : {news_data[0]["title"]}
    Description: {news_data[0]["description"]}
    """,
    from_='+xxxxxxxxxxx',
    to='+xxxxxxxxxxx'
    )
    print(message.sid)
