import json

def load_split(split_path):
    with open(split_path, "r") as f:
        return json.load(f)
