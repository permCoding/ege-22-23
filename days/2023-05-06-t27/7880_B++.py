f = open('./7880_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline())%17 for _ in range(n)]

w = [0] * 17
count = 0

for i in range(n):
    count += w[(17-t[i])%17]
    w[t[i]] += 1
    if i >= k:
        w[t[i-k]] -= 1

print(count)

"""
пример для k = 3
 0  1  2  3  4  5  6  7
17  0 17  0  _  _  _  _  => 6
__  0 17  0  0  _  _  _  => 3

A 15079
B 128655900
"""