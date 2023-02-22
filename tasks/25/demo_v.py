import  re

m = "^1[0-9]{1}2139[0-9]{0,}4$"
r = re.compile(m)

# так очень медленно
# for x in range(10**10+1):
#     s = str(x)
#     if r.search(s) and x%2023==0:
#         print(x, x//2023)

# так быстрее
for x in range(2023, 10**10+1, 2023):
    s = str(x)
    if r.search(s):
        print(x, x//2023)
