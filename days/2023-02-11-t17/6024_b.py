t = list(map(int, open("6024.txt").readlines()))

m = 76123
print(m % 100 == 12)
print(str(m)[-2:] == '12')  # '7612'[-2:]
