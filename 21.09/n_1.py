import re


a='heopfheihf heofih 7 897 9909 щшуарущра аааолол. A46л 4789745кгук Ouoegvbebищмиумю. adfdfau A.B.C.D.'


with open ('n_1.txt', 'w+') as my_file:
    my_file.writelines(a)

with open ('n_1.txt', 'r') as my_file:
    a = my_file.readline()

a=' ' + a + ' '

for i in range (a.count(' ')):

    if (re.search(r'[ ][QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.]+[ ]', a)) != None:
        k = (re.search(r'[ ][QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.]+[ ]', a)).group()
        a = a.replace(((re.search(r'[ ][QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.]+[ ]', a)).group()), ' @')
print(a)
gg = a

for i in range (a.count(' ')):

    if (re.search(r'[ ][уеэоаыяиюЮИЯЭОАЫЕУAaEeYyUuOo]+\w+', a)) != None:
        k = (re.search(r'[ ][уеэоаыяиюЮИЯЭОАЫЕУAaEeYyUuOo]+\w+', a)).group()
        print(k)
        a = a.replace(((re.search(r'[ ][уеэоаыяиюЮИЯЭОАЫЕУAaEeYyUuOo]+\w+', a)).group()), ' ')

for i in range (a.count(' ')):

    if (re.search(r'[ ][1234567890]+[ ]', a)) != None:
        k = (re.search(r'[ ][1234567890]+[ ]', a)).group()
        print(k)
        a = a.replace(((re.search(r'[ ][1234567890]+[ ]', a)).group()), ' ')

dd = re.split(r'[.,/?!:]\s[QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ]', gg)
print(dd)