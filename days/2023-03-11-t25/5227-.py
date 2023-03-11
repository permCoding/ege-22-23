from re import match as m

def check(n):  # это слишком долго
    lst = [d for d in range(1, n//2+1) if n%d==0]
    lst += [n]
    return (len(lst)%2!=0, lst[-1])

for n in range(10**7+1):
    if m('^3.*52.$', str(n)):
        b, d = check(n)
        if b:
            print(n, d)
        