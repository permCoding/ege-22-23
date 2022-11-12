nums = []
for line in open("17.txt").readlines():
    nums.append(int(line))

mx3 = 0
for num in nums:
    if abs(num) % 10 == 3:
        mx3 = max(mx3, num)
print(mx3)

