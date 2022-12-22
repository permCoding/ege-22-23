nums = [int(line) for line in open("5228.txt")][1:]
nums.sort(reverse=True)

pred, count = nums[0], 1
i = 1
while i < len(nums):  # while i
    if pred - nums[i] >= 8:
        pred = nums[i]
        count += 1
    i += 1
print(count, pred)
