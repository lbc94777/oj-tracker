import json
import sys


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
