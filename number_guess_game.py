import random

answer = random.randint(100, 999)

print("数字当てゲーム！！")
print("100から999の数字を当ててください！")

guess = int(input("数字を入力してください: "))

if guess == answer:
    print("正解です！")

else:
    print("不正解です")
    print(f"正解は {answer} でした。")