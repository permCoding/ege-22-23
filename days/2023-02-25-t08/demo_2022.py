from itertools import product as prod

k = 0
for elm in prod('ЕЛМРУ', repeat=4):
    k += 1
    if elm[0]=='Л':
        print(elm, k)
        break
