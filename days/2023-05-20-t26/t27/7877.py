f = open('./27A_7877.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))

sm = 0  # берём минимально возможную
for i in range(0, n-1):  # левый эл-нт пары
    for j in range(i+1, n):  # правый эл-нт пары
        if j-i >= k:  # не менее чем на k
            if (t[i]+t[j])%101 == 0:
                sm = max(sm, t[i]+t[j])
print(sm)
