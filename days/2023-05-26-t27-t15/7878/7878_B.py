f = open('./27B_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))

mx = max(t)
mn, mna, mna157 = mx**2, mx, mx
for i in range(n-k):
    a, b = t[i], t[i+k]
    mna = min(mna, a)
    if a%157==0: mna157 = min(mna157, a)
    if b%157==0: 
        p = mna*b
    else:
        p = mna157*b
    mn = min(mn, p)
print(mn)
        # if p%157==0:
'''
1) если число b само кратно 157 то неважно какое min a
2) если число b НЕ кратно 157 то ВАЖНО какое min a брать
- нам тогда нужно брать min a кратное 157

'''