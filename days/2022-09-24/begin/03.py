def get_for(n, s):
    for _ in range(n):  # от 0 до num-1 включительно
        print(s * n)


def get_while(n, s):
    i = n
    while i > 0:
        print(s * n)
        i -= 1


num = int(input("Введите размер квадрата - "))
smb = input("Введите символ - ")
get_while(num, smb)
