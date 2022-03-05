import json
from os import path

valid_files_json = 'AD2P-valid-files.json'
valid_files = set()

def is_valid_file(file: str) -> bool:
    return path.isfile(file) and path.splitext(file)[1] in valid_files

def load_valid_files():
    json_file = open(valid_files_json)

    json_dump = json.load(json_file)

    for file_type in json_dump:
        valid_files.add(file_type)

    json_file.close()

load_valid_files()