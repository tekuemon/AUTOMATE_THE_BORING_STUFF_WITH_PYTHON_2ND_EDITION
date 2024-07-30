# ライブラリのインポート
import re, sys

# 閏年を判定する関数
def is_leap_year(year):
  year = int(year)
  if year % 4:
    if year % 100:
      if year % 400:
         return True
      else:
           return False
      return False
    return True

# 日付
date = "31/02/2020"

# 正規表現
# date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}')
date_regex = re.compile(r'(0[1-9]|[1-2]\d|3[01])\/(0[1-9]|1[0-2])\/([12]\d{3})')

# 変数の抽出
date_after_regex = date_regex.search(date)

if(date_after_regex == None):
   print("The date is not date.")
   sys.exit(0)

day = date_after_regex.group(1)
month = date_after_regex.group(2)
year = date_after_regex.group(3)

# まずは表示
print("day : " + day)
print("month : " + month)
print("year : " + year)

# 閏年か判定
leap_year_flag = is_leap_year(year)

# 30日までの月を判定
if (
  month == "04" 
  or month == "06"
  or month == "09"
  or month == "11"
):
  if int(day) > 30:
    print("The date is not date.")
    sys.exit(0)

# 2月の日付を判定
if month == "02":
  # 閏年の場合
  if leap_year_flag == True:
    if int(day) > 29:
      print("The date is not date.")
      sys.exit(0)
  # 閏年でない場合
  else:
    if int(day) > 28:
      print("The date is not date.")
      sys.exit(0)

print("The date is truly date.")
