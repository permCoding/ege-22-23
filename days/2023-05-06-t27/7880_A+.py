f = open('./27B_7880.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(0, n-1):  # a
    for b in t[i+1:min(n,i+k+1)]:  # b
        if (t[i]+b)%17 == 0: count += 1
print(count)  # 128655900

"""
k = 3
0 1 2 3 4 5 6 7
b b b a b b b _
a b b b _ _ _ _
_ a b b b _ _ _
"""