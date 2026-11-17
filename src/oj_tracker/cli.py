from oj_tracker import stats, storage


def main() -> None:
    path = "data/records.json"
    days = 7
    records = storage.load_records(path)
    recent_records = stats.recent(records, days)

    print(f"共{len(records)}道题,通过率{stats.ac_rate(records):.1%}")

    print()
    print("标签统计:")
    counts = stats.count_by_tag(records)
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
