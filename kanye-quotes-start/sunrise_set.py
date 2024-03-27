import requests
import datetime as dt
import time
import smtplib
MY_LAT = -0.023559
MY_LONG = 37.906193


def is_up():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()["iss_position"]
    iss_lng = float(iss_data["longitude"])
    iss_lat = float(iss_data["latitude"])
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG+5:
        return True


def is_midnight():
    location = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    today = dt.datetime.now()
    if today.hour > sunset or today.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_up() and is_midnight():
        with smtplib.SMTP("smtp.gmail.com") as connections:
            connections.starttls()
            connections.login(user="clifftest33@gmail.com", password="mjavshcnnjalrzro")
            connections.sendmail(from_addr="clifftest33@gmail.com", to_addrs="clifftest33@gmail.com",
                                 msg="Subject:Look Up\n\nThe ISS is on the sky look up")
