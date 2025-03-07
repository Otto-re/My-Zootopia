import data_fetcher


def escape_html(text):
    """Hilfsfunktion, um sicherzustellen, dass Text für HTML sicher ist."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'",
                                                                                                               "&#39;")


def serialize_animal(animal):
    output_animals = '<li class="cards__item">\n'
    output_animals += f"<div class='card__title'>{escape_html(animal['name'])}</div>\n"
    output_animals += '<p class="card__text">\n'

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output_animals += f"<strong>Diet:</strong> {escape_html(animal['characteristics']['diet'])}<br/>\n"

    if 'locations' in animal and len(animal['locations']) > 0:
        output_animals += f"<strong>Location:</strong> {escape_html(animal['locations'][0])}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output_animals += f"<strong>Type:</strong> {escape_html(animal['characteristics']['type'])}<br/>\n"

    output_animals += '</p>\n'
    output_animals += '</li>\n'
    output_animals += "\n"

    return output_animals


def generate_website(animal_name):
    # Holt die Tiersdaten für das angegebene Tier
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        print("Daten nicht gefunden.")
        return

    # HTML-Vorlage laden
    try:
        with open("animals.html", "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Fehler: animals.html-Datei nicht gefunden.")
        return

    output_animals = ''
    for animal in animals_data:
        output_animals += serialize_animal(animal)

    # Platzhalter in der Vorlage ersetzen
    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_animals)

    # Neue HTML-Datei schreiben
    try:
        with open("animals.html", "w") as file:
            file.write(html_content)
        print("Website wurde erfolgreich in die Datei animals.html generiert.")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")


# Beispielaufruf für "fox"
if __name__ == "__main__":
    animal_name = input("Enter the name of an animal: ")
    generate_website(animal_name)