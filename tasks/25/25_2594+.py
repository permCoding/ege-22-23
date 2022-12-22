print('+')
for n in range(113_000_000, 114_000_001, 2):
    cnt = 0
    for i in range(1, round(n**.5)+1):
        if n%i == 0:
            if i%2==0: cnt += 1
            if (n//i)%2==0: cnt += 1
            if i == n//i: cnt -= 1
            if cnt > 3: break
    if cnt == 3:
        print(n)
print('+')