start = int(0o10000)
stop = int(0o77777)
count = 0
lst = ['16', '36', '56', '76', '67', '65', '63', '61']

for x in range(start, stop+1):
    o = oct(x)[2:]
    if o.count('6') == 1 and all(elm not in o for elm in lst):
        count += 1

print(count)
