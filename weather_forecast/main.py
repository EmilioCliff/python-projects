import requests
from twilio.rest import Client

# lat={lat}&lon={lon}&exclude={part}&appid={API key}
MY_LAT = -0.023559
MY_LONG = 37.906193
account_sid = "twilio_account_sid"
auth_token = "twilio_auth_token"
twilio_number = "twilio_number"
my_api_key = "twilio_api_key"
parameters = {
    "q": "Nairobi",
    # "lat": MY_LAT,
    # "lon": MY_LONG,
    # "exclude": "current,minutely,daily",
    "appid": my_api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()
if weather_data["weather"][0]["id"] > 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='No need of an umbrella',
        from_=twilio_number,
        to='+254718750145'
    )

    print(message.status)
