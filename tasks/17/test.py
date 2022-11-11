def test1():
    nums = []
    mx = -10000
    for line in open("./17.txt"):
        num = abs(int(line))
        nums.append(num)
        if num % 10 == 3:
            mx = max(mx, num)
    print(mx)
    count, mx_sm = 0, 0
    for i in range(len(nums)-1):
        a, b = nums[i], nums[i+1]
        check_a = a % 10 == 3
        check_b = b % 10 == 3
        if check_a ^ check_b:
            sm = a**2 + b**2
            if sm >= mx**2:
                count += 1
                mx_sm = max(sm, mx_sm)

    print(count, mx_sm)


def test2():
    nums = []
    mx = -10000
    for line in open("./17.txt"):
        num = int(line)
        nums.append(num)
        if str(num)[-1] == '3':
            mx = max(mx, num)
    print(mx)
    count, mx_sm = 0, 0
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        check_a = str(a)[-1] == '3'
        check_b = str(b)[-1] == '3'
        if check_a ^ check_b:
            sm = a ** 2 + b ** 2
            if sm >= mx ** 2:
                count += 1
                mx_sm = max(sm, mx_sm)

    print(count, mx_sm)


test1()
test2()

# a = True
# b = False
# print(a ^ b)
