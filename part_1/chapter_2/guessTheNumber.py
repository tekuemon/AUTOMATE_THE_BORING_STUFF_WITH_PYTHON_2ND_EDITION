# 数当てゲーム
import random
secret_number = random.randint(1, 20)
print('1から20までの数を当てて下さい。')

# 6回聞く
for guess_taken in range(1, 7):
    print('数を入力して下さい。')
    guess = int(input())

    if guess < secret_number:
        print('あなたの推定値は小さいです。')
    elif guess > secret_number:
        print('あなたの推定値は大きいです。')
    else:
        break  # 当たり!

if guess == secret_number:
    print('当たり!' + str(guess_taken) + '回で当たりました!')
else:
    print('残念。正解は' + str(secret_number) + 'でした。')
