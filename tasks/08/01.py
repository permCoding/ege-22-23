x = int(0o10000)

count = 0
lst = ['16', '36', '56', '76', '67', '65', '63', '61']
while True:
    o = oct(x)[2:]
    if len(o) > 5:
        break
    if o.count('6') == 1:
        check = True
        for elm in lst:
            if elm in o:
                check = False
                break
        if check:
            count += 1
    x += 1

print(count)
