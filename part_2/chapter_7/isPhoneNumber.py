def is_phone_number(text):
    if len(text) != 12:  # 1
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():  # 2
            return False
    if text[3] != '-':  # 3
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():  # 4
            return False
    if text[7] != '-':  # 5
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():  # 6
            return False
        
    return True  # 7

print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi Moshi は電話番号')
print(is_phone_number('Moshi Moshi'))

message = '明日は415-555-1011に電話してください。オフィスは415-555-9999です。'
for i in range(len(message)):
    chunk = message[i:i+12]  # 1
    if is_phone_number(chunk):  # 2
        print('電話番号が見つかりました: ' + chunk)
print('完了')
