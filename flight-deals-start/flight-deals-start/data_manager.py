import requests
SHEEFT_HEADERS = {
    "Authorization": "Bearer ComeOnGunners",
    "Content-Type": "application/json"
}
prices_sheeft_url = "https://api.sheety.co/c6e0541f57b149461648f49ec783233b/copyOfFlightDeals/prices"
users_sheeft_url = "https://api.sheety.co/c6e0541f57b149461648f49ec783233b/copyOfFlightDeals/users"

class DataManager:
    def read_sheet(self):
        response = requests.get(url=prices_sheeft_url, headers=SHEEFT_HEADERS)
        response.raise_for_status()
        sheet_data = response.json()['prices']
        return sheet_data

    def update_sheet(self, code, row_id):
        upload_data = {
            "price": {
                "iataCode": f"{code}"
            }
        }
        sheeft_put_url = f"https://api.sheety.co/c6e0541f57b149461648f49ec783233b/copyOfFlightDeals/prices/{row_id}"
        response = requests.put(url=sheeft_put_url, json=upload_data, headers=SHEEFT_HEADERS)
        response.raise_for_status()
        
    def get_email(self):
        response = requests.get(url=users_sheeft_url, headers=SHEEFT_HEADERS)
        return response.json()['users']
