import json
import os
path = "data/products.json"
def load_json(path: str) -> dict | list:
#working 19.11.2025
    path = "data/products.json"
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def write_json(path: str, data: dict | list) -> None:
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"Error writing file: {e}")

def ensure_storage_structure(base_dir: str) -> None:
    directories = ['data', 'receipts', 'backups', 'reports']
    for folder in directories:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

def backup_file(source_path: str, backup_dir: str) -> str:
    return
    #backup system