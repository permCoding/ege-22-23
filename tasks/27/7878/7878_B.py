f = open('./27B_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))
mx, mxa, mxe = 10**50, 10**50, 10**50
for i in range(n-k):
    a, b = t[i], t[i+k]
    mxa = min(mxa, a)
    if a%157==0: mxe = min(mxe, a)
    mx = min(mx, (mxa if b%157==0 else mxe)*b)
print(mx)
