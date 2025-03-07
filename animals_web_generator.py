import json
import requests

API_KEY = "UEO0ZcD1Nu20dCIbhInemg==PqkFbhkJjFEQQdwo"
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animal_data(animal_name):
    """Holt Tierdaten von der API"""
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Funktion zur Serialisierung eines einzelnen Tieres
def serialize_animal(animal):
    output_animals = '<li class="cards__item">\n'
    output_animals += f"<div class={'card__title'}>{animal['name']}</div>\n"
    output_animals += '<p class="card__text">\n'
    output_animals += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output_animals += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output_animals += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output_animals += '</p>\n'
    output_animals += '</li>\n'
    output_animals += "\n"

    return output_animals

def main():
    animal_name = input("Enter a name of an animal: ")

    animals_data = fetch_animal_data(animal_name)

    if not animals_data:
        print("Data not found")
        return

# HTML-Vorlage laden
    with open("animals.html", "r") as file:
        template_content = file.read()

    output_animals = ''
    for animal in animals_data:
        output_animals += serialize_animal(animal)

# Platzhalter in der Vorlage ersetzen
    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_animals)

#neue html schreiben
    with open("animals.html", "w") as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()