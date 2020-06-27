import traceback
import json


def load_json_data(path):
    with open(path + ".json") as file:
        data = json.load(file)
    return data


def save_json_data(path, data):
    with open(path + '.json', 'w+') as file:
        json.dump(data, file, sort_keys=False, indent=4, separators=(',', ': '))