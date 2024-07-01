while True:
    age = input('年齢を入力して下さい : ')
    try:
        age = int(age)
    except:
        print('数字を入力して下さい。')
        continue
    if age < 0:
        print('正の数を入力して下さい。')
        continue
    break

print(f'あなたの年齢は{age}です。')
