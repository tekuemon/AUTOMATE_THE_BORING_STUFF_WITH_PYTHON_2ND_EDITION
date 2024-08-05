def spam():
  global eggs  # 1
  eggs = 'spam'  # グローバル変数になる

def bacon():
  eggs = 'bacon'  # ローカル変数になる 2

def ham():
  print(eggs)  # グローバル変数になる 3

eggs = 42  # グローバル変数になる
spam()
print(eggs)