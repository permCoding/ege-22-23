f = open("17.txt")
lines = f.readlines()

mx3 = 0
for line in lines:
    num = int(line)
    # if line[-1] == '3':
    if abs(num) % 10 == 3:
        if num > mx3:
            mx3 = num
print(mx3)


##x = -123
##o = abs(x) % 10
##print(o)

