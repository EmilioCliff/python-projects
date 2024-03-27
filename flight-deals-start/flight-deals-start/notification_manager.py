from twilio.rest import Client
import smtplib
MY_EMAIL = "clifftest33@gmail.com"
MY_PASSWORD = "mjavshcnnjalrzro"
account_sid = "ACd6d10ee3b285cb836efde62b95928230"
auth_token = "929af8e509a3d601855b62819224c30c"
twilio_number = "+12569077962"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
            message = self.client.messages.create(
                body=message,
                from_=twilio_number,
                to="+254718750145"
            )

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"A FLight Offer Just Come Up\n\n{message}"
                )
