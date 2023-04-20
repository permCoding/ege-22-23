def f(a,b,step):
    # print(a,b,step)
    if (a+b) >= 255: return step%2 == 0
    if step == 0: return False

    step -= 1
    f1 = f(a+1,b,step)
    f2 = f(a,b+1,step)
    f3 = f(a*2,b,step)
    f4 = f(a,b*2,step)
    t = [f1,f2,f3,f4]
    if step%2 != 0:
        # return any(t)  # 19  
        return all(t)
    else:
        return any(t)

for s in range(1, 237):
    # if f(17,s,2):  # 19 -> 60: 17,60;17,120;17,240 = 257>=255
    if f(17,s,3) and not(f(17,s,1)):  # 20 -> 110,118: 17,110;34,110;34,220;35,220 = 255>=255 
    # if f(17,s,4) and not(f(17,s,2)):  # 21 -> 109: 
        print(s)
        # break