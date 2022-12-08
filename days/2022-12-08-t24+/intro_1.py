s = 'jab j 2375 427'

cnt = 0
for smb in s:
    if smb == ' ':
        cnt += 1
print(cnt)

cnt = 0
for i in range(0, len(s)):
    if s[i] == ' ':
        cnt += 1
print(cnt)

cnt = 0
i = 0
while i < len(s):
    if s[i] == ' ':
        cnt += 1
    i += 1
print(cnt)
