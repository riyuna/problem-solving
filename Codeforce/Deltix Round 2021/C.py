import sys
input=sys.stdin.readline

pL=[True]*(10**3+1)
primeL=[]
pL[0]=False
pL[1]=False
for i in range(2, 10**3+1):
    if not pL[i]:continue
    primeL.append(i)
    for j in range(i*2, 10**3+1, i):
        pL[j]=False

def isPrime(n):
    if n<1000 and pL[n]:return True
    for i in primeL:
        if n%i==0:return False
    return True

for _ in ' '*int(input()):
    n,e=map(int,input().split())
    L=list(map(int,input().split()))
    ct=0
    for i in range(e):
        ct1=0
        posct=-1
        for j in range(i, n, e):
            if L[j]==1:
                ct1+=1
                ct+=(posct+1)
            elif isPrime(L[j]):
                ct+=ct1
                posct=ct1
                ct1=0
            else:
                ct1=0
                posct=-1
    print(ct)