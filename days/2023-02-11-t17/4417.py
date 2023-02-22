t = list(map(int, open('4417.txt').readlines()))

k, sm = 0, 0
for i in range(len(t)-1):
    for j in range(i+1, len(t)):
        if (t[i]+t[j])%120 == 0:
            k += 1
            sm = max(sm, t[i]+t[j])
print(k, sm)
