# ライブラリのインポート
import re

# Noneの場合は'None'をreturnする関数
def return_ifnotNone(str):
    if str == None:
        return 'None'
    else:
        return str

# 日付
date = '31/02/2020'

# 正規表現
date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}')
# date_regex = re.compile(r'(0[1-9]|[1-2]\d|3[01])\/(0[1-9]|1[0-2])\/([12]\d{3})')

# 変数の抽出
day, month, year = date_regex.search(date)    

# まずは表示
# print('sentence : ' + return_ifnotNone(date_regex.search(date).group()))
print(return_ifnotNone(day) + 
      '/' + return_ifnotNone(month) +
      '/' + return_ifnotNone(year))
