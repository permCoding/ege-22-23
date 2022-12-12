lines = open("./09_2098.csv").readlines()
lst = [list(map(int, line.split(';'))) for line in lines]
print(len([1 for e in lst if e[0]*e[1] == 0 and e[2]*e[3] == 0]))
