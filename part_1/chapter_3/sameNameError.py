def spam():
  print(eggs)  # エラー!
  eggs = 'spam local'  # 1

eggs = 'global'  # 2
spam()
