f = open("17.txt")

lst = [abs(int(line)) for line in f]

max3 = max([x for x in lst if x%10==3])

print(max3, len(lst))

pairs = []
max_sum = -100000
for i in range(len(lst)-1):
    a, b = lst[i], lst[i+1]
    if int(a%10==3) + int(b%10==3) == 1:
        if a**2 + b**2 >= max3**2:
            pairs.append((a,b))
            max_sum = max(max_sum, a**2 + b**2)

print(len(pairs), max_sum)
