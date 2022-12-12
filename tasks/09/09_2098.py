lines = open("./09_2098.csv").readlines()
lst = [line.strip().split(';') for line in lines]
cnt = 0
for elm in lst:
    a = (elm[0] == '0' or elm[1] == '0')
    b = (elm[2] == '0' or elm[3] == '0')
    if a and b: cnt += 1
print(cnt)
