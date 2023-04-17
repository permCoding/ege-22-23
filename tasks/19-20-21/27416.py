def f(a,b,step):
    if a+b >= 77: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
            f(a+1,b,step),
            f(a*2,b,step),
            f(a,b+1,step),
            f(a,b*2,step)
        ]
    #return any(t)  # 19
    if step%2 != 0:
        return all(t)
    else:
        return any(t)

for s in range(1, 70):
    #if f(7,s,2):  # 19 = 18
    #if not(f(7,s,1)) and f(7,s,3):  # 20 = 31 34
    if not(f(7,s,2)) and f(7,s,4):  # 21 = 30
        print(s)
        #break  # 19