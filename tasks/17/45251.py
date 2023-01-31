t = [int(e) for e in  open("./17_45251.txt").readlines()]
m = min([n for n in t if n%21==0])
k, sm = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if a%m==0 or b%m==0:
        k += 1
        sm = max(sm, a+b)
print(k, sm)
