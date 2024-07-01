import pyinputplus as pyip

response = pyip.inputNum('Enter num(min=4) : ', min=4)
print(f'response : {response}')

response = pyip.inputNum('Enter num(greaterThan=4) : ', greaterThan=4)
print(f'response : {response}')

response = pyip.inputNum('Enter num(min=4, lessThan=6) : ', min=4, lessThan=6)
print(f'response : {response}')
