import requests
parameter = {
    "amount": 10,
    "type": "boolean",
    "category": 21
}
response = requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
data = response.json()
response_code = data["response_code"]
question_data = data["results"]
