start = int(0o10000)
stop = int(0o77777)

lst = ['16', '36', '56', '76', '67', '65', '63', '61']
octs = [oct(x)[2:] for x in range(start, stop+1)]
fltr = filter(lambda o: o.count('6') == 1 and all(elm not in o for elm in lst), octs)
print(len(list(fltr)))
