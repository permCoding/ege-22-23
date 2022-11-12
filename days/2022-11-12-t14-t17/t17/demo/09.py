nums = [int(line) for line in open("17.txt")]

mx3 = 0
for num in nums:
    if abs(num) % 10 == 3:
        mx3 = max(mx3, num)

count, sm_m = 0, 0
for i in range(len(nums)-1):
    a, b = nums[i], nums[i+1]
    if (abs(a)%10==3) ^ (abs(b)%10==3):  # XOR
        sm_p = a**2 + b**2
        if sm_p >= mx3**2:
            count += 1
            sm_m = max(sm_m, sm_p)
print(count, sm_m)

'''
a b or and xor == ЛИБО
0 0  0  0  0
0 1  1  0  1
1 0  1  0  1
1 1  1  1  0
'''

