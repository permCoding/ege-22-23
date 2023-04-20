def f(s, step):
    if s >= 68: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
            f(s+1, step),
            f(s+4, step),
            f(s*5, step)
        ]
    if step%2 != 0:
        #return any(t)  # 19
        return all(t)
    else:
        return any(t)


for s in range(1, 68):
    #if f(s,2):  # 19 => 3
    #if not(f(s,1)) and f(s,3):  # 20 => 9 12
    if not(f(s,2)) and f(s,4):  # 21 => 8
        print(s)
        #break
