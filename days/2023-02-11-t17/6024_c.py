t = list(map(int, open("6024.txt").readlines()))

def check(e):
    return e%100 == 12

w = list(filter(check, t))
print(w[:10])

w = list(filter(lambda e: e%100==12, t))
print(w[:10])


w = [e for e in t if e%100==12]
print(w[:10])

w = []
for e in t:
    if e%100 == 12:
        w.append(e)
print(w[:10])
