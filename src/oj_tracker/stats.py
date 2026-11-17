from datetime import date, timedelta


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
