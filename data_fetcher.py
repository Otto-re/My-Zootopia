import requests
import os
from dotenv import load_dotenv


def fetch_data(animal_name):
    load_dotenv()

    API_KEY = os.getenv('API_KEY')
    BASE_URL = "https://api.api-ninjas.com/v1/animals"

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        # Senden der Anfrage an die API
        response = requests.get(BASE_URL, headers=headers, params=params)

        # Überprüfen, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            data = response.json()
            if not data:
                print(f"Kein Ergebnis für {animal_name} gefunden.")
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        # Fehlerbehandlung für Anfragen
        print(f"Es gab einen Fehler bei der Anfrage: {e}")
        return []