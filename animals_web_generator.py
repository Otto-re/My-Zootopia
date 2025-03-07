import data_fetcher

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

def generate_website(animal_name):
    # Holt die Tiersdaten für das angegebene Tier
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        print("Daten nicht gefunden")
        return

    # HTML-Vorlage laden
    with open("animals.html", "r") as file:
        template_content = file.read()

    output_animals = ''
    for animal in animals_data:
        output_animals += serialize_animal(animal)

    # Platzhalter in der Vorlage ersetzen
    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_animals)

    # Neue HTML-Datei schreiben
    with open("animals.html", "w") as file:
        file.write(html_content)

    print("Website wurde erfolgreich in die Datei animals.html generiert.")

# Beispielaufruf für "fox"
if __name__ == "__main__":
    animal_name = input("Enter the name of an animal: ")
    generate_website(animal_name)