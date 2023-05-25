f = open('./27_B_7627.txt')
k = int(f.readline())
n = int(f.readline())
t = list(map(int, f))

mxa, sm = 0, 0
for i in range(n-k):
    mxa = max(mxa, t[i])
    sm = max(sm, mxa + t[i+k])
print(sm)  # 18469835

'''
a + b => max; j-i>=k
0 1 2 3 4 5 6
a _ _ b _ _ _ => tmp = t[0]+t[3]
a a _ _ b     => tmp = max(a) + b
a a a _ _ b   => tmp = max(a) + b
a a a a _ _ b   => tmp = max(a) + b
'''