f = open('./27A_7881.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(e) for e in f]

count = 0
for i in range(0, n-1):  # левый эл-нт пары
    for j in range(i+1, n):  # правый эл-нт пары
        if j-i <= k:
            if (t[i]-t[j])%100 == 0:
                if (t[i]%37==0) ^ (t[j]%37==0):
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