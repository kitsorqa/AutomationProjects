import json


def load_data_from_config():
    with open("../data/data.json", 'r') as f:
        return json.load(f)