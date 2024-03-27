import requests
from twilio.rest import Client

# lat={lat}&lon={lon}&exclude={part}&appid={API key}
MY_LAT = -0.023559
MY_LONG = 37.906193
account_sid = "ACd6d10ee3b285cb836efde62b95928230"
auth_token = "929af8e509a3d601855b62819224c30c"
twilio_number = "+12569077962"
my_api_key = "f17eab2854fd8ac1eb02db51e2bf2005"
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
