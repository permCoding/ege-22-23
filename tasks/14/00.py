x = 12
b = bin(x)
print(b)

o = oct(x)
print(o)

h = hex(x)
print(h)

s = '0x' + 'FF'
print(int(s, 16))

s = '0o' + '10'
print(int(s, 8))

s = '0b' + '1100'
print(int(s, 2))

num1 = '0x' + '12'
num2 = '0x' + '08'
res = hex(int(num1,16)+int(num2,16))
print(res[2:].upper())
print(int(res,16))
