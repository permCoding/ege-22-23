from re import match as m

def check(n):  # ускорим
    sqrt = n**.5
    b, d = False, 0
    if int(sqrt)==sqrt:
        b = True
        for i in range(2, n//2+1):
            if n%i==0:
                d = n//i
                break
    return (b, d)

for n in range(10**7+1):
    if m('^3.*52.$', str(n)):
        b, d = check(n)
        if b:
            print(n, d)
        