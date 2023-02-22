t = list(map(int, open("6024.txt").readlines()))
w = [e for e in t if e%100==12]

m = 0
for e in w:
    if e>m:
        m = e
print(m)


