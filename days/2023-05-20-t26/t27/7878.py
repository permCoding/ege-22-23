f = open('./27A_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))
# n = 4
# k = 1
# t = [2,3,1,4]  # 6 2 8 3 12 4
sm = 2_000_000 ** 2  # берём максимально возможное для пары
for i in range(0, n-1):  # левый эл-нт пары
    for j in range(i+1, n):  # правый эл-нт пары
        if j-i >= k:  # не менее чем на k
            if (t[i]*t[j])%157 == 0:
                sm = min(sm, t[i]*t[j])
                # if t[i]*t[j] < sm:
                #     sm = t[i]*t[j]
print(sm)
