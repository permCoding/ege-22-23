n = 1
while 1 == 1:
    b = bin(n)[2:]
    cnt = b.count('1')
    if cnt % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 40:
        print(n)
        break
    n += 1

