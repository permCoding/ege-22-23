def check(o):
    return o.count('6')==1 and all(elm not in o for elm in lst)


start = int(0o10000)
stop = int(0o77777)

lst = ['16', '36', '56', '76', '67', '65', '63', '61']
octs = [oct(x)[2:] for x in range(start, stop+1)]

print(len(list(filter(check, octs))))
