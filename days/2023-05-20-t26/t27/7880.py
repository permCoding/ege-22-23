f = open('./27A_7880.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(0, n-1):  # левый эл-нт пары
    for j in range(i+1, n):  # правый эл-нт пары
        if j-i <= k:  # расстояние не более чем k
            if (t[i]+t[j])%17 == 0:
                count += 1
print(count)

'''
a b r
0 0 0
0 1 1
1 0 1
1 1 0
XOR ^
'''