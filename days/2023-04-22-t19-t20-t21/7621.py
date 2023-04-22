# 17 10
def f(s, step):
    if s >= 43: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [f(s+1, step), f(s+4, step), f(s*3, step)]
    return all(t)  # 19
    #return any(t) if step%2 == 0 else all(t)

for s in range(1, 43):  # П1 - В1 - П2 - В2
    if f(s, 2):  # 19 => 5
    #if not(f(s,1)) and f(s,3):  # 20 => 10 13
    #if not(f(s,2)) and f(s,4):  # 21 => 9
        print(s)
        #break