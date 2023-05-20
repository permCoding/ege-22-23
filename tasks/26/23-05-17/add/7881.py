f = open('./27A_7881.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(e) for e in f]

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if j-i <= k:
            if (t[i]-t[j])%100 == 0:
                if (t[i]%37==0) ^ (t[j]%37==0):
                    count += 1
print(count)
