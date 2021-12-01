from math import gcd
pL=[True]*3001
pL[0]=False
pL[1]=False
prime=[]
for i in range(2,3001):
    if not pL[i]:continue
    prime.append(i)
    for j in range(i*2, 3001, i):pL[j]=False
    
def getdivisor(n):
    if n==1:return {1}
    if n<3000 and pL[n]:return {1, n}
    pr=True
    for i in prime:
        if n%i==0:
            pr=False
            break
    if pr:return {1, pr}
    ct=0
    while n%i==0:
        ct+=1
        n//=i
    prm=i
    res=getdivisor(n)
    newres=set()
    for i in res:
        for j in range(ct+1):
            newres.add(i*pow(prm,j))
    return newres
    
# print(getdivisor(10))
# print(getdivisor(121))
# print(getdivisor(1001))
# print(getdivisor(1024))
    
n=int(input())
L=list(map(int,input().split()))
L.sort()
div_ind=[[] for i in range(n)]
rem=dict()
for i in range(n):
    for j in getdivisor(L[i]):
        if j in rem:
            div_ind[i].append(rem[j])
    rem[L[i]]=i
    
dp=[L[i]-1+n for i in range(n)]
for i in range(n):
    for j in div_ind[i]:
        dp[i]=max(dp[i], dp[j]+L[i]-1)
mx=0
g=0
for i in range(n):
    g=gcd(g, L[n-i-1])
    mx+=g
print(max(mx, max(dp)))