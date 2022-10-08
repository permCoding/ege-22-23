b = '111001'

sm = 0
for smb in b:
    sm += int(smb)
print(sm)

sm = 0
for i in range(len(b)):
    sm += int(b[i])
print(sm)
