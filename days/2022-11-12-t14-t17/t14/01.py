print("task-14 - demo")
alph = '0123456789abcde'

for x in alph:
    a = int(f'123{x}5', 15)
    b = int(f'1{x}233', 15)
    r = a + b
    if r % 14 == 0:
        print(r//14)
        break
