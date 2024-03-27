import requests
from newsapi import NewsApiClient
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = "MSIIYEVU2F5WHJCU"
news_api_key = "bf577350348c4e66a8c4a4318a898d4c"
account_sid = "ACd6d10ee3b285cb836efde62b95928230"
auth_token = "929af8e509a3d601855b62819224c30c"
twilio_number = "+12569077962"

# Getting closing values of two previous days from stockapi
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
x = 0
two_day_data = [{key: value} for idx, (key, value) in enumerate(stock_data["Time Series (Daily)"].items()) if idx < 2]
previous_day_date = list(stock_data["Time Series (Daily)"])[0]
before_previous_day_date = list(stock_data["Time Series (Daily)"])[1]
previous_day_close = float(two_day_data[0][previous_day_date]["4. close"])
before_previous_day_close = float(two_day_data[1][before_previous_day_date]["4. close"])
difference = before_previous_day_close - previous_day_close
percentage = round((difference*100)/previous_day_close, 2)
increased = f"Tesla is up by 🔺{percentage}"
if difference < 0:
    increased = f"Tesla went down by 🔻{percentage}"

# Getting relevant news regarding tesla inc from newsapi
client = NewsApiClient(api_key=news_api_key)
tesla_article = client.get_everything(
    q=COMPANY_NAME,
    from_param=before_previous_day_date,
    to=previous_day_date,
    language="en",
    sort_by="popularity"
)
tesla_article_title = tesla_article["articles"][30]["title"]
tesla_article_description = tesla_article["articles"][30]["description"]

# Sending the message to a number
client = Client(account_sid, auth_token)
message = client.messages \
        .create(
    from_=twilio_number,
    to="+254718750145",
    body=f"{increased}\nSubject:  {tesla_article_title}\n\n{tesla_article_description}"
)
print(message.status)
