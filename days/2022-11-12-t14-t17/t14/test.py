def get():
    return 3


x = 8
num = '123' + str(x) + '5'
print(num)

s = f'123{x}5'
print(s)

s = f'123{get()}5'
print(s)
