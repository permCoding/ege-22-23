f = open('./27A_7876.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(e) for e in f]

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if j-i >= k:
            if (t[i]+t[j])%120 == 0:
                # x = (t[i]%41!=0) and (t[j]%41==0)
                # y = (t[i]%41==0) and (t[j]%41!=0)
                # if x or y:
                if (t[i]%41==0) ^ (t[j]%41==0):  # XOR
                    cnt += 1
print(cnt)

'''
a b r
0 0 0
0 1 1
1 0 1
1 1 0
'''
