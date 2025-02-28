import json

# load the json data in read mode
def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r") as file:
    template_content = file.read()

output_animals = ''
for animal in animals_data:
    output_animals += '<li class="cards__item">\n'
    output_animals += f"<div class={"card__title"}>{animal['name']}</div>\n"
    output_animals += '<p class="card__text">\n'
    output_animals += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output_animals += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output_animals += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output_animals += '</p>\n'
    output_animals += '</li>\n'
    output_animals += "\n"


html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output_animals)

with open("animals.html", "w") as file:
    file.write(html_content)
