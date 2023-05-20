f = open('./26_6031.txt')
n = int(f.readline())

# t = list(map(int, f))
# t.sort(reverse=True)

# t = sorted(map(int, f), reverse=True)

t = sorted(map(int, f))[::-1]

print(t[:20])