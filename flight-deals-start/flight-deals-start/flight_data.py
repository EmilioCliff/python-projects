class FlightData:
    def __init__(self, city_from, city_from_code, city_to, city_to_code, flight_price, flight_day, return_day,
                 stopovers=0, city_to_stopover=""):
        self.city_from = city_from
        self.city_from_code = city_from_code
        self.city_to = city_to
        self.city_to_code = city_to_code
        self.flight_price = flight_price
        self.flight_day = flight_day
        self.return_day = return_day
        self.stopover = stopovers
        self.city_to_stopover = city_to_stopover
