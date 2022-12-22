import re


for i in range(2023, 10**10, 2023):
    if re.match(r'^1.2139.*4$', str(i)):
        print(i, i//2023)


# import fnmatch
# import re

# reg = fnmatch.translate('1?2139*4')
# print(reg)

# reg = re.match(r'^1.2139.*4$', '1521393104')
# print('True' if reg else 'False')