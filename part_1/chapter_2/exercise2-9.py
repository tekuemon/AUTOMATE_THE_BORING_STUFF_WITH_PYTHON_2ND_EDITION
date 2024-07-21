import random

spam = random.randint(1, 3)
print('spam : ' + str(spam))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
