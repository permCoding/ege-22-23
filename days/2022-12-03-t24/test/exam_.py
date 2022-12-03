x = 65
y = 20
print(x % y, x // y)

a = b = 0
while a < 5:
    a += 1
    b += 2
print(b)

a = b = 0
while a < 5:
    a += 1
    b += a
print(b)

a = b = 0
while a < 5:
    b += a
    a += 1
print(b)

a, b, s = 0, 9, ''
while a < b:
    a, b = a+1, b-1
    s += '1'
print(s)

a, b, s = 0, 5, '1'
while a < b:
    a, b = a+1, b-1
    s *= 2
print(s)

s = 'qwerty'
print(s[0] + s[-1])
print(s[::1])
print(s[::2])
print(s[::-1])

t = [1,3,2,4,0]
print(t[0], t[-1])
print(t[1:3])
print(t[::-1])
sm = 0
for i in range(len(t)):
    if t[i] % 2 != 0:
        sm += t[i]
print(sm)
