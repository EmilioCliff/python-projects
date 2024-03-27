import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "clifftest33@gmail.com"
my_password = "mjavshcnnjalrzro"
zooka_headphones_url = "https://www.jumia.co.ke/zoook-zg-rambo-professional-gaming-headset-army-color-32553389.html"

response = requests.get(zooka_headphones_url)
website_data = BeautifulSoup(response.text, "html.parser")
name = website_data.find("h1", class_="-fs20 -pts -pbxs").getText()
price = float("".join(website_data.find("span", dir="ltr").getText().split()[1].split(",")))
if price < 3000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        message = connection.sendmail(
            msg=f"Discount Alert!!\n\nThe price of the {name} has a discount to {price}. Buy Now!!!{zooka_headphones_url}",
            from_addr=my_email,
            to_addrs="emiliocliff@gmail.com"
        )