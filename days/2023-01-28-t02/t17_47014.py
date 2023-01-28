lines = open("17_47014.txt").readlines()
nums = [int(line) for line in lines]
f = [num for num in nums if num%2!=0]
avg = sum(f) / len(f)

k, sm = 0, 0
for i in range(len(nums)-1):
    a, b = nums[i], nums[i+1]
    u1 = a%5==0 and b<avg
    u2 = b%5==0 and a<avg
    if int(u1) ^ int(u2):
        k += 1
        sm = max(sm, a+b)

print(k, sm)
