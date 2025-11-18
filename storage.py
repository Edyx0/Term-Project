import json
path = "data/products.json"
def load_json(path: str) -> dict | list:
    #json file reaching must be fixed
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def write_json(path: str, data: dict | list) -> None:
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"Error writing file: {e}")

def ensure_storage_structure(base_dir: str) -> None:
    return
    #check storage working properly

def backup_file(source_path: str, backup_dir: str) -> str:
    return
    #backup system