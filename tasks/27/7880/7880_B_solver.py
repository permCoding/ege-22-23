f = open('./7880_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

# n = 8
# k = 6
# t = [2,4,17,15,13,19,9,8]

# n = 5
# k = 3
# t = [17,17,17,17,17]

d = 17
w = [0] * d
for i in range(k+1): w[t[i]%d] += 1
print(w)

nn = w[0]-1
tmp = sum([w[i]*w[d-i] for i in range(1, d//2+1)]) + (1+nn)*nn//2
print(tmp)

for i in range(n-k-1):
    w[t[i]%d] -= 1
    pos = t[i+k+1]%d
    tmp += w[(d-pos)%17]
    w[pos] += 1
    print(w)    
    print(tmp)


"""
пример для k = 3
 0  1  2  3  4  5  6  7
17  0 17  0  _  _  _  _  => 6
__  0 17  0  0  _  _  _  => 3

A 15079
B 128655900
"""