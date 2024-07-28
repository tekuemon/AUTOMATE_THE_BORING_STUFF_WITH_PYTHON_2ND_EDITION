import re

def print_ifnotNone(str):
    if str == None:
        print('None')
    else:
        print(str.group())

Watanabe_regex = re.compile(r'[A-Z][a-z]+\sWatanabe')

name1 = 'Haruto Watanabe'  # ヒットする
name2 = 'Alice Watanabe'  # ヒットする
name3 = 'Robocop Watanabe'  # ヒットする
name4 = 'haruto Watanabe'  # ヒットしない
name5 = 'Mr. Watanabe'  # ヒットしない
name6 = 'Watanabe'  # ヒットしない
name7 = 'Haruto watanabe'  # ヒットしない


print_ifnotNone(Watanabe_regex.search(name1))
print_ifnotNone(Watanabe_regex.search(name2))
print_ifnotNone(Watanabe_regex.search(name3))
print_ifnotNone(Watanabe_regex.search(name4))
print_ifnotNone(Watanabe_regex.search(name5))
print_ifnotNone(Watanabe_regex.search(name6))
print_ifnotNone(Watanabe_regex.search(name7))
