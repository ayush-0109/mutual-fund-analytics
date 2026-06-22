import requests

funds = {
    "SBI Small Cap Fund": "125497",
    "HDFC Flexi Cap Fund": "118834",
    "ICICI Prudential Bluechip Fund": "120503",
    "Nippon India Growth Fund": "118778",
    "Parag Parikh Flexi Cap Fund": "122639"
}

for fund_name, amfi_code in funds.items():
    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n" + "="*50)
        print("Fund:", fund_name)
        print("NAV Date:", data["data"][0]["date"])
        print("NAV:", data["data"][0]["nav"])
    else:
        print(f"Error fetching {fund_name}")