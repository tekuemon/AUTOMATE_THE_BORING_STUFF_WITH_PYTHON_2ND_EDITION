while True:
    print('あなたはだれ?')
    name = input()
    if name != 'Joe':  # 1
        continue  # 2
    print('こんにちはJoe。パスワードは何?(魚の名前)')
    password = input() # 3
    if password == 'swordfish':
        break  # 4
print('認証しました。')  # 5
