t = [int(e) for e in open("17_47221.txt").readlines()]
m = -999999999
for e in t:
    if (e>0 and e%10==3) or (e<0 and e%10==7):
        if e>m:
            m = e

k, sm = 0, 0
for i in range(len(t)-1):
    a,b = t[i],t[i+1]
    if a*a+b*b >= m**2:
        if (str(a)[-1]=="3") ^ (str(b)[-1]=="3"):
            k+=1
            sm = max(sm, a*a+b*b)
print(k, sm)
"""
58
"""
