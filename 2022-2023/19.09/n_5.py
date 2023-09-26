with open ('haplology.TXT', 'r', buffering = 1, encoding=" utf-8") as my_file:
    a=my_file.readlines()
for i in range(len(a)):
    b=a[i]
    a[i]=b[0:-1]
print(a)
k=1
def haplology(s, l):
    for i in range(len(s)+1-l):
        chek=s[i:i+l]

        if s.count(chek)>1:
            s=s.replace(chek, '.')
            toch=(s.count(chek))*'.'
            s = s.replace(toch, '')
            for i in range(s.count('.')-1):
                s=s.replace(".", "", 1)
            s=s.replace('.', chek)

    return(s)
k=0
for n in range (len(a)):

    for i in range(2, len(a[n])):
        a[n]=haplology(a[n], i)
print(a)



