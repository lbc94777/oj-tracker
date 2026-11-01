import json


def main() -> None:
    path = "data/records.json"
    records = load_records(path)
    print(records)


def load_records(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
        return records


def save_records(records, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
