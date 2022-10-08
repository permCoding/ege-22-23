n = 1
while True:
    b = bin(n)[2:]
    sm = 0
    for smb in b:
        sm += int(smb)
    if sm % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    if int(b, 2) > 40:
        print(n)
        break
    n += 1
