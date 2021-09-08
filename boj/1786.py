import math
n=int(input())
L1=input().split()
L2=input().split()
t=''
p=''

t="".join(L1)
t+=t

p="".join(L2)

fail=[0]*len(p)
i,j=0,0
for i in range(1,len(p)):
    while j>0 and p[i]!=p[j]:
        j=fail[j-1]
    if p[i]==p[j]:
        j+=1
        fail[i]=j
    else:
        fail[i]=0
ct=0
pt=0

for i in range(len(t)-1):
    while pt>0 and t[i]!=p[pt]:
        pt=fail[pt-1]
    
    if t[i]==p[pt]:
        if pt==len(p)-1:
            ct+=1
            pt=fail[pt]
        else:pt+=1

gcd = math.gcd(n,ct)
print(f'{ct//gcd}/{n//gcd}')