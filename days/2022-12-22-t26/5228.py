nums = [int(line) for line in open("5228.txt")][1:]
nums.sort(reverse=True)

pred, count = nums[0], 1
for num in nums[1:]:  # for nums
    if pred - num >= 8:
        pred = num
        count += 1
print(count, pred)

# for i
# while i
