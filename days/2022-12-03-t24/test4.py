s = '121 99 1009797 333'

print(len(s))

lst = ['12', '34', '56']
print(' - '.join(lst))

s = ''.join(lst)  # 123456
print(s[1:4])
print(s[1:-1])
print(s[:])
print(s[::2])
print(s[::-1])

s = 'Абракадабра'
print(s.upper())
print(s.lower())

s = 'A10BB'
for smb in s:
    print(smb, smb.isdigit())
