# 2-1
- True
  - '真'を表す値
- False
  - '偽'を表す値

# 2-2
- and
  - 両方Trueであるか
- or
  - 少なくとも一方がTrueであるか
- not
  - 値の否定

# 2-3
|  | and | or |
| --- | --- | --- |
| 両方False | False | False |
| 一方のみTrue | False | True |
| 両方True | True | True |

|  | not |
| --- | --- |
| True | False |
| False | True |

# 2-4
- (5 > 4) and (3 == 5)
  - False
- not (5 > 4)
  - False
- (5 > 4) or (3 == 5)
  - True
- not ((5 > 4) or (3 == 5))
  - False
- (True and True) and (True == False)
  - False
- (not False) or (not True)
  - True

# 2-5
- ==
  - 値が等しいか
- !=
  - 値が等しくないか
- <
  - より小さい
- <=
  - より小さいか等しい
- \> 
  - より大きい
- \>=
  - より大きいか等しい

# 2-6
等価比較演算子は左右の値が等しいかを判定する。
代入演算子は左の変数に右の値を代入する。

# 2-7
条件式は式の値がTrueかFalseであるかを判定する。
if文、while文、for文などで使う

# 2-8
- ブロック1 : l2:l8
- ブロック2 : l4:l5
- ブロック3 : l6:l7

# 2-9
exercise2-9.py にて

# 2-10
Ctrl + c

# 2-11
- breakはループ文を抜け出す
- continueはループ文の最初に遷移する

# 2-12
- forループでrange(10), range(0, 10), range(0, 10, 1)はいずれも[0, 9]の範囲で1ずつ増加する。

# 2-13
exercise2-13.pyにて

# 2-14
spam.bacon()

# 発展問題
- round()
  - 第1引数に丸め対象の値、第2引数に丸め桁数を与え、丸めた値を返す
- abs()
  - 引数の値の絶対値を返す