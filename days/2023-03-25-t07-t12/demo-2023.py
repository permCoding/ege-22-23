def is_prime(n):
    # b = False
    for d in range(2, n):
        if n % d == 0:
            return False
    # else:
        # переписать это
    return True

n = 0
while True:
    s = '>' + '0'*39 + '1'*n + '2'*39
    while ('>1' in s) or ('>2' in s) or ('>0' in s):
        if '>1' in s: s = s.replace('>1','22>',1)
        if '>2' in s: s = s.replace('>2','2>',1)
        if '>0' in s: s = s.replace('>0','1>',1)

    r = sum(map(int, s.replace('>','')))
    print(r)
    if is_prime(r):
        print(n, r)
        break
    
    n += 1
