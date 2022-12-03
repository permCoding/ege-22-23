# len
# split
# [::]
# replace
# join
# find
# count

# strip
# isdigit
# upper lower

# PEP 8

s = '121|99|1009797|333'
lst = s.split('|')
print(lst)
print(max(lst))

mx = 0
for elm in lst:
    if int(elm) > mx:
        mx = int(elm)
print(mx)




if '99999999' > '9A':
    print(99)
else:
    print(100)
