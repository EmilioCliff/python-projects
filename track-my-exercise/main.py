import requests
import datetime as dt
APP_ID = "f2ca7ba5"
API_KEY = "876d285dd9a117feeaaa3843784d3185"
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrients_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
sheety_exercise_endpoint = f"https://api.sheety.co/c6e0541f57b149461648f49ec783233b/myWorkouts/sheet2"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
headers = {
    "Authorization": "Bearer ThisIsSecret",
    "Content-Type": "application/json"
}
date = dt.datetime.now().date()
time = dt.datetime.now().time().replace(microsecond=0)
sheet = ['sheet1', 'sheet2']
which_sheet = 2

if which_sheet == 1:
    query_data_exercise = {
        # "query":
        "query": input("Tell me about your workout today: "),
        "gender": "male",
        "weight_kg": 83.5,
        "height_cm": 170.00,
        "age": 22
    }
    response_exercise = requests.post(url=f"{exercise_url}", headers=HEADERS, json=query_data_exercise)
    response_exercise.raise_for_status()
    exercise_data = response_exercise.json()
    for i in range(len(exercise_data['exercises'])):
        row_data = {
            "sheet1": {
                "date": f"{date}",
                "time": f"{time}",
                "exercise": f"{exercise_data['exercises'][i]['name']}",
                "duration": f"{exercise_data['exercises'][i]['duration_min']}",
                "calories": f"{exercise_data['exercises'][i]['nf_calories']}"
            }
        }
        sheety_exercise_endpoint = f"https://api.sheety.co/c6e0541f57b149461648f49ec783233b/myWorkouts/sheet1"
        response_upload_exercise = requests.post(url=sheety_exercise_endpoint, json=row_data, headers=headers)
        response_upload_exercise.raise_for_status()

else:
    query_data_nutrients = {
        "query": input("What did you eat today? ")
    }
    response_nutrients = requests.post(url=nutrients_url, json=query_data_nutrients, headers=HEADERS)
    response_nutrients.raise_for_status()
    nutrients_data = response_nutrients.json()
    for i in range(len(nutrients_data['foods'])):
        row_dta = {
            "sheet2": {
                "date": f"{date}",
                "time": f"{time}",
                "foodName": f"{nutrients_data['foods'][i]['tags']['item']}",
                "measure": f"{nutrients_data['foods'][i]['tags']['measure']}",
                "quantity": f"{nutrients_data['foods'][i]['tags']['quantity']}",
                "protein": f"{nutrients_data['foods'][i]['nf_protein']}",
                "sugars": f"{nutrients_data['foods'][i]['nf_sugars']}",
                "fats": f"{nutrients_data['foods'][i]['nf_total_fat']}"
            }
        }
        sheety_exercise_endpoint = f"https://api.sheety.co/c6e0541f57b149461648f49ec783233b/myWorkouts/sheet2"
        response_upload_nutrients = requests.post(url=sheety_exercise_endpoint, json=row_dta, headers=headers)
        response_upload_nutrients.raise_for_status()
sheet_data = requests.get(url=sheety_exercise_endpoint, headers=headers)
