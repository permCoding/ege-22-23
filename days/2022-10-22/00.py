dec = 12

b = bin(dec)
o = oct(dec)
h = hex(dec)

print(b)  # 0b1100
print(o)  # 0o14
print(h)  # 0xc

h1 = 0x19
h2 = 0x18
res = hex(h1 + h2)

print(int(res, 16))

b = '0b1101'
print(int(b, 2))




# bin - 01 | _1_0
# oct - 01234567 | _1_01234567
# dec - 0123456789 | _1_0123456789
# hex - 0123456789ABCDEF | _1_0123456789ABCDEF

# 19(10) + 1(10) = 20(10)
# 17(8) + 3(8) = 22(8)
# 19(16) + 1(16) = 1A(16)
# 19(16) + 3(16) = 1C(16)
# 19(16) + 16(16) = 2F(16)
# 19(16) + 18(16) = 31(16)