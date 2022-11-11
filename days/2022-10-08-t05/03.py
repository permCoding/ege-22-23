import os

os.system('cls')

# ver 1
for n in range(1, 1000):
    b = bin(n)[2:]  # 1. Строится двоичная запись числа N
    cnt = b.count('1')
    if cnt % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    r = int(b, 2)
    if r > 40:
        print(n)
        break 

# ver 2
# n = 1
# while True:
#     pass
#     pass
#     if r > 40:
#         print(n)
#         break
#     n += 1