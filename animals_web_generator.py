import json

# load the json data in read mode
def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

# find name, diet, locations and if type there the type in json data
for animal in animals_data:
    if "name" in animal:
        print(f"Name: {animal["name"]}") #show name of fox
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print(f"Diet: {animal["characteristics"]["diet"]}") #show diet of fox
    if "locations" in animal:
        print(f"Locations: {animal["locations"][0]}") #show location of fox
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print(f"Type: {animal["characteristics"]["type"]}") #show type of fox if its there elso dont show this
    print() # a clear line for better readebles


