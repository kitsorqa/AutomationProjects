import json


def load_config():
    with open('../config/data.json', 'r') as file:
        return json.load(file)