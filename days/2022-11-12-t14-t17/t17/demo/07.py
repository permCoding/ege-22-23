nums = [int(line) for line in open("17.txt").readlines()]

mx3 = 0
for num in nums:
    if abs(num) % 10 == 3:
        mx3 = max(mx3, num)

count = 0
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    if (a%10==3 and b%10!=3) or (a%10!=3 and b%10==3):
        count += 1
print(count)
