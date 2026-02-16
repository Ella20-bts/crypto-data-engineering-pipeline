import requests
import json
from datetime import datetime
import os
import time

def extract_crypto_data():
    base_url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"raw_data/crypto_{timestamp}.json"

    os.makedirs("raw_data", exist_ok=True)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Extracted {len(data)} coins")
    print(f"✅ Data saved to {filename}")

    return data
