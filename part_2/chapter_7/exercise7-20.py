import re

def print_ifnotNone(str):
    if str == None:
        print('None')
    else:
        print(str.group())

num_regex = re.compile(r'^\d{1,3}(,\d{3})*$')

number1 = '42'  # ヒットする
number2 = '1,234'  # ヒットする
number3 = '6,368,745'  # ヒットする
number4 = '12,34,567'  # ヒットしない
number5 = '1234'  # ヒットしない

print_ifnotNone(num_regex.search(number1))
print_ifnotNone(num_regex.search(number2))
print_ifnotNone(num_regex.search(number3))
print_ifnotNone(num_regex.search(number4))
print_ifnotNone(num_regex.search(number5))
