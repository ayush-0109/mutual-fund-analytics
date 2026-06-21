import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print(data["meta"]["scheme_name"])
print(data["data"][0])