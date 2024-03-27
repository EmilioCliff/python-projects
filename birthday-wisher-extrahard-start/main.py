import pandas
import random
import datetime as dt
import smtplib
from details import my_email, my_password

data = pandas.read_csv("birthdays.csv")
birthdays_data = data.to_dict(orient="records")
print(birthdays_data)
today = dt.datetime.now()
for i in range(len(birthdays_data)):
    if birthdays_data[i]["month"] == today.month and birthdays_data[i]["day"] == today.day:
        letter_to_open = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
        with open(f"letter_templates/{letter_to_open}", "r") as letter:
            my_letter = letter.read()
            updated_letter = my_letter.replace("[NAME]", f"{birthdays_data[i]['name']}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_data[i]["email"],
                msg=f"Subject: Happy Birthday {birthdays_data[i]['name']}\n\n{updated_letter}"
            )
