# 10:25
def f(a,b,step):
    if a+b>=82: return step%2==0
    if step==0: return False
    step -= 1
    t = [
            f(a+1,b,step),f(a,b+1,step),
            f(a*4,b,step),f(a,b*4,step)
        ]
    # return any(t)  # 19
    return any(t) if step%2==0 else all(t)

for s in range(1,78):
    # if f(4,s,2):  # 19 => 5
    # if not(f(4,s,1)) and f(4,s,3):  # 20 => 16 19
    if not(f(4,s,2)) and f(4,s,4):  # 20 => 18
        print(s)
        # break
