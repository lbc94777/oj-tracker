import json


def load_records(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
        return records


def save_records(records, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def count_by_tag(records):
    count = {}
    for record in records:
        tags = record["tags"]
        for tag in tags:
            count[tag] = count.get(tag, 0) + 1
    return count


def all_tags(records):
    s = set()
    for record in records:
        tags = record["tags"]
        for tag in tags:
            s.add(tag)
    return s


def main() -> None:
    path = "data/records.json"
    records = load_records(path)
    # print(records)
    print(count_by_tag(records))
    print(all_tags(records))
