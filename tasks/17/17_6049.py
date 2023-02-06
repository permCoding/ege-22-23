t = [int(e) for e in open("./17_6049.txt").readlines()]
m = max([e for e in t if str(e)[-1] == '9'])
k, sm = 0, 999999999
for i in range(len(t)-1):
    a,b = t[i], t[i+1]
    u1 = str(a)[-1] == '9'
    u2 = str(b)[-1] == '9'
    if (u1 ^ u2) and a*a+b*b < m*m:
        k += 1
        sm = min(sm, a*a+b*b)
print(k, sm)        
    