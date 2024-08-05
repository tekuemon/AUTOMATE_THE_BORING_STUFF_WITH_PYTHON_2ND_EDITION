def spam():
  eggs = 'spam local'  # 1
  print(eggs)  # 'spam local'を表示

def bacon():
  eggs = 'bacon local'  # 2
  print(eggs)  # 'bacon local'を表示
  spam()
  print(eggs)  # 'bacon local'を表示
eggs = 'global'  # 3
bacon()
print(eggs)  # 'global'を表示
