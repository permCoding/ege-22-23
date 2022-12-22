nums = [int(line) for line in open("demo.txt")][1:]
nums.sort(reverse=True)

pred, count = nums[0], 1
for num in nums[1:]:
    if pred - num >= 3:
        pred = num
        count += 1
print(count, pred)  # count max(min())

# for i
# while i
# for nums