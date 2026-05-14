# 简易记账小工具
balance = 0

import random 
encouragements = [
    "加油！理性消费，攒钱超有成就感！",
    "你已经很棒了，继续保持记账好习惯！",
    "管住手，未来的你会感谢现在的自己~",
    "每一笔记录，都是在为你的财务自由铺路！"
]
# 随机给个存钱建议
suggestions = ["别乱花钱！", "存点钱买个喜欢的东西吧！", "再省一点就能攒够啦！"]
print("💡 小建议：", random.choice(suggestions))

while True:
    print("\n" + random.choice(encouragements))
    print("===== 个人记账 =====")
    print("1 收入")
    print("2 支出")
    print("3 查看余额")
    print("0 退出")
    print("5 小彩蛋：查看今日运势")

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
    elif choice == "5":
        print("✨ 今日运势：大吉！适合攒钱，不适合乱花钱~")

    else:
        print("输入错误，请重新选择")