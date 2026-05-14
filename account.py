# 简易记账小工具
balance = 0

while True:
    print("===== 个人记账 =====")
    print("1 收入")
    print("2 支出")
    print("3 查看余额")
    print("0 退出")

    choice = input("请选择功能：")

    if choice == "1":
        money = float(input("输入收入金额："))
        balance += money
        print(f"收入成功！当前余额：{balance} 元")

    elif choice == "2":
        money = float(input("输入支出金额："))
        balance -= money
        print(f"支出成功！当前余额：{balance} 元")

    elif choice == "3":
        print(f"当前余额：{balance} 元")

    elif choice == "0":
        print("退出记账程序")
        break
    else:
        print("输入错误，请重新选择")