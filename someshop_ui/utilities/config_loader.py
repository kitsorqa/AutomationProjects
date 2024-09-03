import json


def load_config():
    with open('someshop_ui/config/data.json', 'r') as file:
        return json.load(file)