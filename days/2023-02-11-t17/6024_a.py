t = open("6024.txt").readlines()

t = list(map(int, t))
print(t[:10])

t = [int(e) for e in t]
print(t[:10])
