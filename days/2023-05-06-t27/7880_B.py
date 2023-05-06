f = open('7880_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

d = 17
count = 0
for i in range(0, n-k):  # a
    for j in range(i+1, i+k):  # b
        a, b = t[i], t[j]
        if (a+b)%d == 0: count += 1
print(count)
"""
k = 3
0 1 2 3 4 5 6
a b b b _ _ _

0 1 2 3 4 5 6
b a b b b _ _

0 1 2 3 4 5 6
b b a b b b _

0 1 2 3 4 5 6
b b b a b b b

0 1 2 3 4 5 6
_ b b b a b b

"""