lst = [1,2,3,4,5,6]
print(lst.pop())
print(lst)

lst += [1,1,1]
lst.append(999)
lst += [888]
print(lst)

print('- - - - - - - -')

lst = ["1","2","3"]
print(".".join(lst))

lst = [111,222,333]
# print(".".join(lst))  # так нельзя

print(" . ".join([str(elm) for elm in lst]))

print(" . ".join(map(str, lst)))

print('- - - - - - - -')

lst = [4,2,4,4]
lst.append(0)
print(lst)

lst_e = [6,6,7]
lst.extend(lst_e)
print(lst)

st = {0, 0}
st.add(1)
st.add(1)
print(st)

lst = [4,2,4,4]
st = set(lst)
print(st)
st_b = set([0,0,0,1])
st = st | st_b  # объединение множеств
print(st)

a, b = {4,3,0}, {7,0,3,666}
set_all = a & b  # пересечение множеств
print(set_all)
