import json


def open_file_json(file_json):
    with open(file_json, encoding='utf-8') as file:
        readfile = json.load(file)
    return readfile
