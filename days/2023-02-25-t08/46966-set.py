from itertools import permutations as perm

st = set()
sg, gl = 'РСХМ', 'ОА'
for word in perm('РОСОМАХА'):
    b = True
    for i in range(len(word)-1):
        usla = (word[i] in sg) and (word[i+1] in sg)
        uslb = (word[i] in gl) and (word[i+1] in gl)
        if usla or uslb:
            b = False
    if b:
        st.add(word)
print(len(st))

# не должны стоять рядом две гласные
# и две согласные буквы
