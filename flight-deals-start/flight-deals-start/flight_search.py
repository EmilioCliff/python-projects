import requests
from flight_data import FlightData

API_KEY = "iP7jSjB1cNO_7YASdehjPOgSn7EgPcy1"
HEADER = {
    "apikey": f"{API_KEY}"
}
search_endpoint = "https://api.tequila.kiwi.com/v2/search"
location_endpoint = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    def get_city_code(self, cityname):
        parameter = {
            "term": f"{cityname}",
            "location_types": "airport"
        }
        response = requests.get(url=location_endpoint, params=parameter, headers=HEADER)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def search_engine(self, from_destination, to_destination, from_date, to_date):
        search_data = {
            "fly_from": f"{from_destination}",
            "fly_to": f"{to_destination}",
            "date_from": f"{from_date}",
            "date_to": f"{to_date}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "KES",
            "max_stopovers": 0
        }
        response = requests.get(url=search_endpoint, params=search_data, headers=HEADER)
        try:
            flight_data = response.json()['data'][0]
        except IndexError:
            search_data['max_stopovers'] = 1
            response = requests.get(url=search_endpoint, params=search_data, headers=HEADER)
            flight_data = response.json()
            # print(flight_data)
            if flight_data['_results'] > 0:
                dst_name = flight_data['data'][0]['route'][1]['cityTo']
                dst_iata = flight_data['data'][0]['route'][1]['flyTo']
                current_name = flight_data['data'][0]['route'][0]['cityFrom']
                current_iata = flight_data['data'][0]['route'][0]['flyFrom']
                price = flight_data['data'][0]['price']
                departure_date = flight_data['data'][0]['route'][0]['local_departure'].split("T")[0]
                return_date = flight_data['data'][0]['route'][2]['local_departure'].split("T")[0]
                via_city = flight_data['data'][0]["route"][0]["cityTo"]
                stop_overs = 1
                flight = FlightData(current_name, current_iata, dst_name, dst_iata, price,
                                    departure_date, return_date, stop_overs, via_city)
                return flight
            else:
                return None

        else:
            dst_name = flight_data['route'][0]['cityTo']
            dst_iata = flight_data['route'][0]['flyTo']
            current_name = flight_data['route'][0]['cityFrom']
            current_iata = flight_data['route'][0]['flyFrom']
            price = flight_data['price']
            departure_date = flight_data['route'][0]['local_departure'].split("T")[0]
            return_date = flight_data['route'][1]['local_departure'].split("T")[0]
            flight = FlightData(current_name, current_iata, dst_name, dst_iata, price,
                                departure_date, return_date)
            return flight
