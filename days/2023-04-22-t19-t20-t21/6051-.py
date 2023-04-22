# 31 38
def f(a,b,step):
    if a+b >= 52: return step%2 == 0
    if step == 0: return False
    step -= 1
    x = f(a+2,b,step)
    y = f(a,b+2,step)
    m = f(a*3,b,step)
    n = f(a,b*3,step)
    #return any(t)  # 19
    #return any(t) if step%2==0 else all(t) # 20, 21
    if step%2 == 0:
        return x or y or m or n  # хотя бы один
    else:
        return x and y and m and n  # при любом

for s in range(1, 47):
    #if f(5, s, 2):  # 19 => 6
    #if not(f(5,s,1)) and f(5,s,3):  # 20 => 5 6
    if not(f(5,s,2)) and f(5,s,4):  # 21 => 14
        print(s)
