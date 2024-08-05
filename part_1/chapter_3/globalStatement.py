def spam():
  global eggs  # 1
  eggs = 'spam'  # 2
eggs = 'global'
spam()
print(eggs)
