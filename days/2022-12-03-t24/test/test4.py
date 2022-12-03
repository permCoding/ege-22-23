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

s = '121 99 1009797 333'
print(s.replace(' ', ';', 1))
print(s.replace(' ', ';'))

print(s.find(' '))
print(s.find(' ', 7))

print(s.count(' '))
print(s.count(' ', 7))

s = '   121 99 1009797 333\n'
print(len(s))
s = s.strip()
print(s)
print(len(s))


s = '1\t99\n100   9797\n333\n'
print(s)
