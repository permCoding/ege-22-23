f = open('./27A_7880.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

d = 17
count = 0
for i in range(0, n-1):  # a
    for j in range(i+1, min(n,i+k+1)):  # b
        a, b = t[i], t[j]
        if (a+b)%d == 0: count += 1
print(count)

"""
k = 3
0 1 2 3 4 5 6 7
b b b a b b b _
a b b b _ _ _ _
_ a b b b _ _ _
"""