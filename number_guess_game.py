import random
import time

answer = random.randint(100, 999)
max_attempts = 10
attempts = 0
start_time = time.time()

print("数字当てゲーム！！")
print("100から999の数字を当ててください！")
print(f"回答できる回数は{max_attempts}回です！")

while attempts < max_attempts:
    guess = int(input("数字を入力してください: "))
    attempts += 1

    if guess == answer:
        elapsed_time = time.time()-start_time
        print("正解です！")
        print(f"{attempts}回目で正解しました")
        print(f"かかった時間：{elapsed_time:.1f}秒")
        break

    print("不正解です")

    if guess < answer:
        print("もっと大きい数字です")
    else:
        print("もっと小さい数字です")

    difference = abs(answer-guess)

    if difference <= 10:
        print("かなり近いです！")

    elif difference <= 50:
        print("少し近いです")

    else:
        print("まだ離れています")

    print(f"残り{max_attempts - attempts}回です")

if guess != answer:
    print("ゲームオーバーです")
    print(f"正解は{answer}でした")