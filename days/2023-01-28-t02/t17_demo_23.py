lines = open("17.txt").readlines()
nums = [int(line) for line in lines]

k, sm = 0, 0
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    u1 = str(a)[-1]=='3' and str(b)[-1]!='3'
    u2 = str(a)[-1]!='3' and str(b)[-1]=='3'
    if (u1 or u2) and (a*a + b*b >= 9973**2):
            k += 1
            sm = max(sm, a*a + b*b)
print(k, sm)

# 1 число оканч на 3
# a**2+b**2 >= m**3
# m = макс эл-нт посл оканч на 3 = 9973
# 180 
