f = open('./27_A_7627.txt')
k = int(f.readline())
n = int(f.readline())
t = list(map(int, f))
# k = 3
# n = 5
# t = [15,2,0,10,30]

mxa, sm = 0, 0
for i in range(n-k):
    a, b = t[i], t[i+k]
    # mxa = max(t[0:i+1])
    mxa = 0
    for j in range(0, i+1):
        if t[j]>mxa:
            mxa = t[j]
    sm = max(sm, mxa + b)
print(sm)

'''
a + b => max; j-i>=k
0 1 2 3 4 5 6
a _ _ b _ _ _ => tmp = t[0]+t[3]
a a _ _ b     => tmp = max(a) + b
a a a _ _ b   => tmp = max(a) + b
a a a a _ _ b   => tmp = max(a) + b
'''