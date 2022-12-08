s = 'AABCDOEODRABRR'
lst_g = ['A','E','O']
cnt_g = 0
for smb in s:
    if smb in lst_g:
        cnt_g += 1
cnt_s = len(s)-cnt_g
print(cnt_g, cnt_s)
