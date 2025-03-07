import os
import requests
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()

# API-Key und Basis-URL
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if not data:
                print(f"Kein Ergebnis für {animal_name} gefunden.")
            return data
        else:
            print(f"Fehler: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")
        return []


def generate_html(data):
    html_content = "<html><head><title>Animal Information</title></head><body><h1>Tierdaten</h1>"

    if data:
        html_content += "<table border='1'><tr><th>Name</th><th>Wissenschaftlicher Name</th><th>Lebensraum</th><th>Beschreibung</th></tr>"
        for animal in data:
            html_content += f"<tr><td>{animal.get('name', 'N/A')}</td><td>{animal.get('scientific_name', 'N/A')}</td><td>{animal.get('habitat', 'N/A')}</td><td>{animal.get('description', 'N/A')}</td></tr>"
        html_content += "</table>"
    else:
        html_content += "<p>Keine Daten gefunden.</p>"

    html_content += "</body></html>"

    with open("animals.html", "w") as file:
        file.write(html_content)
        print("HTML-Datei erfolgreich generiert!")


def main():
    while True:
        animal_name = input("Gib den Namen eines Tieres ein (oder 'exit' zum Beenden): ").lower()
        if animal_name == 'exit':
            break

        data = fetch_data(animal_name)
        generate_html(data)


if __name__ == "__main__":
    main()