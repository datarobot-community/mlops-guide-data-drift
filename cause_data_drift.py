import datarobot as dr
import requests
import json

# read file
with open('resources/drifting_cars.json', 'r') as file:
    data = file.read()

# parse file
drifting_cars = json.loads(data)

DATAROBOT_API_TOKEN = "YOUR_API_TOKEN"
DATAROBOT_ROOT_URL = "https://app2.datarobot.com" # Your DataRobot URL
DATAROBOT_API_URL = "{DATAROBOT_ROOT_URL}/api/v2"
DATAROBOT_DEPLOYMENT_ID = "YOUR_DEPLOYMENT_ID" # You deployment ID - same as the project from quick start

prediction_headers = {
    "Authorization": f"Bearer {DATAROBOT_API_TOKEN}",
    "Content-Type": "application/json; charset=UTF-8"
}

r = requests.post(f"{DATAROBOT_API_URL}/deployments/{DATAROBOT_DEPLOYMENT_ID}/predictions", 
    json = drifting_cars, 
    headers = prediction_headers)

print(r.status_code)
print(r.text)
