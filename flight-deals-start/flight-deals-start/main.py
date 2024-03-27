from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
FROM = "NBO"
data = DataManager()
flight = FlightSearch()
approved = NotificationManager()

today = datetime.now().date()
date_after_6_months = today + timedelta(days=(6*30))
sheet_data = data.read_sheet()
email_data = data.get_email()
if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight.get_city_code(row['city'])
        data.update_sheet(row['iataCode'], row['id'])

for row in sheet_data:
    my_flight = flight.search_engine(FROM, row['iataCode'], today.strftime("%d/%m/%Y"), date_after_6_months.strftime("%d/%m/%Y"))
    if my_flight is not None and my_flight.flight_price < row['lowestPrice']:
        emails = [row['email'] for row in email_data]
        message = (f"Low Price Alert\n Only {my_flight.flight_price}Ksh to fly from "
                   f"{my_flight.city_from}-{my_flight.city_from_code} to"
                   f" {my_flight.city_to}-{my_flight.city_to_code} "
                   f"from {my_flight.flight_day} to {my_flight.return_day}")
        if my_flight.stopover == 1:
            message += f" and has {my_flight.stopover} stopover via {my_flight.city_to_stopover}"

        approved.send_email(emails, message)
        # approved.send_sms(message)
