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
    # 返回records内的tag统计情况
    count = {}
    for record in records:
        tags = record["tags"]
        for tag in tags:
            count[tag] = count.get(tag, 0) + 1
    return count


def all_tags(records):
    # 返回records内的tag种类
    return {tag for record in records for tag in record["tags"]}


def ac_rate(records):
    # 返回records内的ac率
    if len(records) == 0:
        return 0
    count = 0
    for record in records:
        if record["ac"]:
            count += 1
    rate = count / len(records)
    return rate


def recent(records, days=7):
    # 返回days内的数据
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
    # print(records)
    # print(count_by_tag(records))
    # print(all_tags(records))
    # print(ac_rate(records))
    # print(recent(records))
    # print(recent(records, days=-1))
    # print(all_tags(records))
    # print(titles_by_difficulty(records, "入门"))
    days = 7
    records = load_records(path)
    recent_records = recent(records, days)

    print(f"共{len(records)}道题,通过率{ac_rate(records):.1%}")

    print()
    print("标签统计:")
    counts = count_by_tag(records)
    for tag, n in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"  {tag}  {n}")

    print()
    print(f"最近 {days} 天的记录:")
    if not recent_records:
        print("  没有近期记录")
    for record in recent_records:
        status = "通过" if record["ac"] else "未通过"
        tags = "、".join(record["tags"])
        print(
            f"  {record['date']}  {record['id']}  {status}  "
            f"{record['title']}({record['difficulty']},{tags})"
        )


if __name__ == "__main__":
    main()
