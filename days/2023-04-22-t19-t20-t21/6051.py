# 31 38
def f(a,b,step):
    if a+b >= 52: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
        f(a+2,b,step),
        f(a,b+2,step),
        f(a*3,b,step),
        f(a,b*3,step)
    ]
    #return any(t)  # 19
    return any(t) if step%2==0 else all(t) # 20, 21

for s in range(1, 47):
    #if f(5, s, 2):  # 19 => 6
    #if not(f(5,s,1)) and f(5,s,3):  # 20 => 5 6
    if not(f(5,s,2)) and f(5,s,4):  # 21 => 14
        print(s)
