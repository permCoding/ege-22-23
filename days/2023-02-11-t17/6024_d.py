t = list(map(int, open("6024.txt").readlines()))
m = max([e for e in t if e%100==12])
print(m)


