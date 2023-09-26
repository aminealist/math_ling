from math import comb

n = int(input())
k=''
for i in range(n):
        koef=comb(n,i)
        k=k+str(koef)+'x^'+str(n-i)+'+'
print(k[1:-3]+'+1')