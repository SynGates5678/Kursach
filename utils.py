import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
         return json.load(f)

def save_json(data, filename):
     with open(filename, 'w', encoding='utf-8') as f:
         json.dump(data, f, ensure_ascii=False, indent=4)