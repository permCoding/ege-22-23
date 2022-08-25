def check(o):
    return 1 if o.count('6')==1 and all(elm not in o for elm in lst) else 0


start, stop = int(0o10000), int(0o77777)

lst = ['16', '36', '56', '76', '67', '65', '63', '61']

print(sum([check(oct(x)[2:]) for x in range(start, stop+1)]))
