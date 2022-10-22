# https://inf-ege.sdamgia.ru/problem?id=9367

x = 9**8 + 3**5 - 9
cnt = 0
while x > 0:
    if x % 3 == 2:
       cnt += 1  # cnt = cnt + 1
    x //= 3 
print(cnt)

'''
Значение арифметического выражения: 
9**8 + 3**5 – 9
записали в системе счисления с основанием 3. 
Сколько цифр «2» содержится в этой записи?

10000000000000000
+
00000000000100000
-
00000000000000100
-----------------
?????????????????
'''