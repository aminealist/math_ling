import re


a='heopfheihf heofih 7 897 9909 щшуарущра аааолол adfdfau A.B.C.D.'


with open ('n_1.txt', 'w+') as my_file:
    my_file.writelines(a)

with open ('n_1.txt', 'r') as my_file:
    a = my_file.readline()

print(re.search(r'^[уеэоаыяиюЮИЯЭОАЫЕУ]', a))