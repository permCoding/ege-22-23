f = open('./27B_7880.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(0, n-1):  # a
    for b in t[i+1:min(n,i+k+1)]:  # b
        if (t[i]+b)%17 == 0: count += 1
print(count)

# 15079
# 128655900
