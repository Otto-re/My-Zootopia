import data_fetcher
import os


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

    if 'locations' in animal and animal['locations']:
        output_animals += f"<strong>Location:</strong> {escape_html(animal['locations'][0])}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output_animals += f"<strong>Type:</strong> {escape_html(animal['characteristics']['type'])}<br/>\n"

    output_animals += '</p>\n</li>\n'  # Korrektur hier
    return output_animals


def generate_website(animal_name):
    animals_data = data_fetcher.fetch_data(animal_name)
    if not animals_data:
        print("Daten nicht gefunden.")
        return

    template_file = "animals_site.html"  # Verwenden der Vorlage
    output_file = "animals.html"  # Die generierte Datei

    if not os.path.exists(template_file):
        print(f"Fehler: {template_file} nicht gefunden.")
        return

    with open(template_file, "r", encoding="utf-8") as file:
        template_content = file.read()

    output_animals = ''.join(serialize_animal(animal) for animal in animals_data)
    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_animals)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Website erfolgreich generiert: {output_file}")


if __name__ == "__main__":
    animal_name = input("Enter the name of an animal: ")
    generate_website(animal_name)