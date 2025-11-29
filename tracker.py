import json
from datetime import datetime

DATA_FILE = "data.json"

# 初始化数据文件
def init_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

# 保存数据
def save_data(records):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

# 添加记录
def add_record(amount, category, note=""):
    records = init_data()
    records.append({
        "amount": amount,
        "category": category,
        "note": note,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_data(records)

# 读取记录
def list_records():
    return init_data()

# 统计汇总
def summary():
    records = init_data()
    income = sum(r["amount"] for r in records if r["amount"] > 0)
    expense = sum(-r["amount"] for r in records if r["amount"] < 0)
    return income, expense, income - expense
