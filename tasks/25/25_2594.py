print('+')
for n in range(113_000_000, 114_000_001, 2):
    divs = set([n])
    for i in range(1, round(n**.5)+1):
        if n%i == 0:
            if i%2==0: divs.add(i)
            if (n//i)%2==0: divs.add(n//i)
            if len(divs) > 3: break
    if len(divs) == 3:
        print(n, sorted(divs))
print('+')