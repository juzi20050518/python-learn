import random

def guess_number():
    target = random.randint(1, 100)
    print("猜数字游戏！数字在1-100之间")
    while True:
        guess = int(input("请输入你的猜测："))
        if guess < target:
            print("太小了！")
        elif guess > target:
            print("太大了！")
        else:
            print("恭喜你猜对了！")
            break

if __name__ == "__main__":
    guess_number()