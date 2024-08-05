# ライブラリのインポート
import sys

def collatz(number):
  if number % 2 == 0:  # number が偶数なら
    return number / 2  # 戻り値は number / 2
  elif number % 2 == 1:  # number が奇数なら
    return 3 * number + 1  # 戻り値は 3 * number + 1

print("数字を入力してください:")
try:
  userinput = int(input())  # ユーザに整数を入力してもらう
except ValueError:  # 被整数の文字列が入力された場合
  print("整数値を入力してください")  # 整数値を入力するように示すメッセージを表示
  sys.exit()
collatzresult = collatz(userinput)

while True:
  print(collatzresult)
  if(collatzresult == 1):  # collatz関数が1を返したらbreak
    break
  collatzresult=int(collatz(collatzresult))
