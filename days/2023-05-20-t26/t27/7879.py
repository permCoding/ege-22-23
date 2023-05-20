f = open('./27A_7879.txt')
n = int(f.readline())
k = int(f.readline())
t = []
for e in f:
    t.append(int(e))

sm = 0
for i in range(0, n-1):  # левый эл-нт пары
    for j in range(i+1, n):  # правый эл-нт пары
        if j-i >= k:  # не менее чем на k
            if (t[i]+t[j])%2023 == 0:
                if (t[i]%47==0) ^ (t[j]%47==0):
                    sm = max(sm, t[i]+t[j])
                    # if t[i]+t[j] > sm:
                    #     sm = t[i]+t[j]
print(sm)
