import json
import os

def load_json(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def write_json(path, data):
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print("Error writing file: " + str(e))

def ensure_storage_structure(base_dir):
    directories = ['data', 'receipts', 'backups', 'reports']
    for folder in directories:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

def backup_file(source_path, backup_dir):
    return