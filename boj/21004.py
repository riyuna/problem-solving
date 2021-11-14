from math import log2, gcd
from functools import reduce
pList=[]
erat=[True]*1000001
erat[0]=False
erat[1]=False
for i in range(2, 1001):
    if not erat[i]:continue
    pList.append(i)
    for j in range(i*2, 10**6+1, i):
        erat[i]=False

def fact(n):
    if n==1 or erat[n]:return [n]
    for p in pList:
        if n%p==0:
            return fact(n//p)+[p]

def fact2(n):
    d=dict()
    for i in fact(n):
        if i==1:continue
        if i not in d:d[i]=0
        d[i]+=1
    L=[]
    for i in d:
        L.append((i, d[i]))
    return L

def divisorGen(n):
    if n==1:return [1]
    factors = list(fact2(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    ct=0
    d=dict()
    for i in L:
        if i not in d:d[i]=0
        d[i]+=1
    for i in d:
        for j in divisorGen(i):
            if j==i:continue
            if int(log2(i))==int(log2(i-j)) and (i-j)&j==0 and i-j in d:
                if gcd(i,i-j)!=i^(i-j):assert(0)
                ct+=(d[i]*d[i-j])
    print(ct)