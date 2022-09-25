import re


a='8 913 924-42-27 ... 8 913 916 32 27 ... 89245338458 ...' \
  ' 8-905-672-32-33 ... +7 913 926-48-43 ... +7 913 567 32 37' \
  ' ... +79243898328 ... +7-905-672-32-34'
#просьба не звонить -_-


with open ('n_2.txt', 'w+') as my_file:
    my_file.writelines(a)

with open ('n_2.txt', 'r') as my_file:
    a = my_file.readline()

a=' ' + a + ' '

print((re.findall (r'[+][1234567890]{1,3}[ ][1234567890]{3}', a)))




#for i in range (a.count(' ')):

    #if (re.search(r'\b[+123456789 0-]+', a)) != None:
        #k = (re.search(r'\b[+123456789 0-]+', a)).group()
        #print(k)
        #a = a.replace(((re.search(r'', a)).group()), ' ')