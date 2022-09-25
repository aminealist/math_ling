from random import shuffle


kk = input()
n=[]
for i in range(int(kk)):
    n.append(i+1)
k = ''

for i in range(len(n) * 10000):
    shuffle(n)
    b=''
    for i in range(len(n)):
        b+=str(n[i])
    if k.count(b)<1:
        k = k + b + ' . '
print(k.count('.'))