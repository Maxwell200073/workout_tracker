import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv('C:/Users/maxwe/OneDrive/Desktop/.env')
time_now = datetime.datetime.now().strftime('%H:%M')
today = datetime.datetime.now().strftime('%m/%d/%Y')
# print(today)
params = {
    'query': input('What exercise did you do today? '),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 175.26,
    "age": 32
}
endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': os.getenv('nut_appId'),
    'x-app-key': os.getenv('nut_key')
}
response = requests.post(url=endpoint, headers=headers, data=params)
response.raise_for_status()
result = response.json()
items = result['exercises']

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    url = 'https://api.sheety.co/c0a730d5ac5287f6dffdb42cffbcecb7/myWorkouts/workouts'
    s_response = requests.post(url=url, json=sheet_inputs)
    s_response.raise_for_status()
    print(s_response.text)

