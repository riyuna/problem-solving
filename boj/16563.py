import sys

pList=[True]*(10**4+1)
pList[0]=False
pList[1]=False
pl=[]
for i in range(2, 10**4+1):
    if not pList[i]:continue
    pl.append(i)
    for j in range(i*2, 10**4+1, i):
        pList[j]=False

rem=dict()

def isPrime(n):
    if n<10**4 and pList[n]:return True
    for i in pl:
        if n%i==0:return False
    return True

def fact(n):
    if n in rem:return rem[n]
    if isPrime(n):
        rem[n]=[n]
        return [n]
    for p in pl:
        if n%p==0:
            L=fact(n//p)[:]
            L.append(p)
            L.sort()
            rem[n]=L
            return L


n=int(input())
nList=list(map(int,input().split()))
for i in nList:
    L=fact(i)
    for j in L:print(j, end=' ')
    print()