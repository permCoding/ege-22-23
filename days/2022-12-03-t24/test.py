
x = 49   # 110001
s = '1'  # 110001

smb = chr(49)

print(smb + smb + smb)
print(ord(smb))

for i in range(48, 60):
    print(i, chr(i), bin(i)[2:])

for smb in 'ABCDEF':
    print(smb, ord(smb))
