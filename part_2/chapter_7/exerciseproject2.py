# ライブラリのインポート
import re

# 強いパスワードか確認する関数
def is_password_strong(password):
  # 8文字以上であるか
  password_strong_regex_1 = re.compile(r'.{8,}')
  # 大文字と小文字を含むか
  password_strong_regex_2 = re.compile(r'[A-Za-z]+')
  # 1つ以上の数字を含むか
  password_strong_regex_3 = re.compile(r'[0-9]')

# パスワードの入力
password = input()

