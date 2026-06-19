

import requests

def extract():
    url = "https://v6.exchangerate-api.com/v6/c5188215018796a0f0a6ccae/latest/USD"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    raise Exception(
        f"Failed to fetch data. Status code: {response.status_code}"
    )

if __name__ == "__main__":
    print(extract())

    
