def F(n):
    multi = 1
    for i in range(1, n+1):
        multi *= i
    return multi

print(F(2023)//F(2020))
# 1 2 3 4 ... 2019 2020 2021 2022 2023
# 1 2 3 4 ... 2019 2020