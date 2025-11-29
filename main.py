from tracker import add_record, list_records, summary

def menu():
    print("\n====== 简单记账工具 ======")
    print("1. 添加记录")
    print("2. 查看记录")
    print("3. 查看汇总")
    print("4. 退出")

while True:
    menu()
    choice = input("请输入选项：")

    if choice == "1":
        amount = float(input("金额（收入正数，支出负数）："))
        category = input("类别（如：餐饮/工资/购物）：")
        note = input("备注：")
        add_record(amount, category, note)
        print("记录已添加！")

    elif choice == "2":
        records = list_records()
        print("\n===== 所有记录 =====")
        for r in records:
            print(f"{r['time']} | {r['category']} | {r['amount']} | {r['note']}")

    elif choice == "3":
        income, expense, balance = summary()
        print("\n===== 汇总 =====")
        print("总收入：", income)
        print("总支出：", expense)
        print("结余：", balance)

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效选项，请重试！")
