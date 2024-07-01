import pyinputplus as pyip

response = pyip.inputNum('Enter num(limit=2) : ', limit=2)
print(response)

response = pyip.inputNum('Enter num(timeout=10) : ', timeout=10)
print(response)
