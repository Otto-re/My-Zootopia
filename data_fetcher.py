import requests

def fetch_data(animal_name):
    API_KEY = "UEO0ZcD1Nu20dCIbhInemg==PqkFbhkJjFEQQdwo"
    BASE_URL = "https://api.api-ninjas.com/v1/animals"

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if not data:
            print(f"Kein Ergebnis für {animal_name} gefunden.")
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []