
a, b = 312, 5112

print((a%100==12) ^ (b%100==12))

# OR XOR

for x in 0,1:
    for y in 0,1:
##        print(x,y, x or y)
        print(x,y, x ^ y)  # только один
