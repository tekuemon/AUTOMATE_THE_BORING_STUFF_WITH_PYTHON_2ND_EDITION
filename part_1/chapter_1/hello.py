# このプログラムは挨拶を表示して名前と年齢を尋ねる 1

print('Hello, world!')  # 2
print('What is your name?')  # 名前を尋ねる
my_name = input()  # 3
print('It it good to meet you, ' + my_name)  # 4
print('The length of your name is:')  # 名前の長さを表示 5
print(len(my_name))
print('What is your aege?')  # 年齢を尋ねる 6
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')  # 来年の年齢を表示