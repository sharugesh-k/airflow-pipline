import requests

def extract():
    url="https://v6.exchangerate-api.com/v6/c5188215018796a0f0a6ccae/latest/USD"
    auth_token ="c5188215018796a0f0a6ccae"
    params={"auth_token": auth_token}
    response = requests.get(url, params=params)
    if response.status_code == 200 :
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")
    
data_exchange=extract()
print(data_exchange)

    
