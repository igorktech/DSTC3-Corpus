import traceback
import json


def load_json_data(path, file_name):
    try:
        with open(path + file_name + ".json") as file:
            data = json.load(file)

    except (IOError, ValueError):
        traceback.print_exc()
        return False

    return data


def save_json_data(path, file_name, data):
    with open(path + file_name + '.json', 'w+') as file:
        json.dump(data, file, sort_keys=False, indent=4, separators=(',', ': '))