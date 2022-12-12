lines = open("./09_2100.txt").readlines()
lst = [sorted(map(int, e.split('\t'))) for e in lines]
print(max([e[0]+e[1] for e in lst if e[0]*e[0] + e[1]*e[1] == e[2]*e[2]]))

