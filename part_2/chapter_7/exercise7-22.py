import re

def print_ifnotNone(str):
    if str == None:
        print('None')
    else:
        print(str.group())

sentence_regex = re.compile(r'(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$', re.IGNORECASE)

sentence1 = 'Alice eats apples.'  # ヒットする
sentence2 = 'Bob pets cats.'  # ヒットする
sentence3 = 'Carol throws baseballs.'  # ヒットする
sentence4 = 'Alice throws Apples.'  # ヒットする
sentence5 = 'BOB EATS CATS.'  # ヒットする
sentence6 = 'RoboCop eats apples.'  # ヒットしない
sentence7 = 'ALICE THROWS FOOTBALLS.'  # ヒットしない
sentence8 = 'Carol eats 7 cats.'  # ヒットしない

print_ifnotNone(sentence_regex.search(sentence1))
print_ifnotNone(sentence_regex.search(sentence2))
print_ifnotNone(sentence_regex.search(sentence3))
print_ifnotNone(sentence_regex.search(sentence4))
print_ifnotNone(sentence_regex.search(sentence5))
print_ifnotNone(sentence_regex.search(sentence6))
print_ifnotNone(sentence_regex.search(sentence7))
print_ifnotNone(sentence_regex.search(sentence8))
