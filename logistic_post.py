import requests
import json

url = "http://192.168.1.74:5000/api/"

payload = json.dumps([
  [
    0.24923,
    -0.31685,
    -0.67825,
    -0.30033,
    -1.55521,
    1.63088,
    -1.37983,
    -1.54858,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ]
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
