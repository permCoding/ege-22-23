lst, max3 = [], 0
for line in open("17.txt"):
    elm = abs(int(line))
    lst.append(elm)
    if elm % 10 == 3:
        max3 = max(max3, elm)

print(max3, len(lst))

cnt, max_sum = 0, 0
for i in range(len(lst) - 1):
    a, b = lst[i], lst[i + 1]
    if (a % 10 == 3) ^ (b % 10 == 3):
        if a ** 2 + b ** 2 >= max3 ** 2:
            cnt += 1
            max_sum = max(max_sum, a ** 2 + b ** 2)

print(cnt, max_sum)
