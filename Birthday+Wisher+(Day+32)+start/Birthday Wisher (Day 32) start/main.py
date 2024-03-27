import smtplib
import datetime as dt
import random
from details import my_email, my_password, recipient_email

with open("quotes.txt", "r") as data:
    quotes = data.readlines()
    quote_of_the_day = random.choice(quotes)

now = dt.datetime.now()
if now.weekday() == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Tuesday Quote\n\n{quote_of_the_day}"
                            )
