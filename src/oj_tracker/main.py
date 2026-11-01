import json
import sys
from datetime import date, timedelta


def load_records(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            records = json.load(f)

    except FileNotFoundError:
        print("找不到数据文件:", path)
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"数据文件 '{path}' 已损坏,第{e.lineno}行附近,请修复该文件或从备份恢复.")
        sys.exit(1)

    else:
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
    s = {tag for record in records for tag in record["tags"]}
    return s


def ac_rate(records):
    count = 0
    for record in records:
        if record["ac"]:
            count += 1
    if len(records) == 0:
        return 0
    rate = count / len(records)
    return round(rate, 2)


def recent(records, days=7):
    if days < 0:
        raise ValueError(f"天数不能为负数:{days}")

    start = (date.today() - timedelta(days=days)).isoformat()
    result = [record for record in records if record["date"] >= start]
    return result


def titles_by_difficulty(records, level):
    titles = [record["title"] for record in records if record["difficulty"] == level]
    return titles


def main() -> None:
    path = "data/records.json"
    records = load_records(path)
    print(records)
    # print(count_by_tag(records))
    # print(all_tags(records))
    # print(ac_rate(records))
    # print(recent(records))
    # print(recent(records, days=-1))
    # print(all_tags(records))
    # print(titles_by_difficulty(records, "入门"))
