from itertools import permutations as perm

st = set()
for word in perm('РОСОМАХА'):
    sm0, sm1 = 0, 0
    for i in 0,2,4,6:
        if word[i] in 'РСХМ': sm0 += 1
        if word[i+1] in 'РСХМ': sm1 += 1
    if sm0 == 4 or sm1 == 4:
        st.add(word)
print(len(st))

# не должны стоять рядом две гласные
# и две согласные буквы
