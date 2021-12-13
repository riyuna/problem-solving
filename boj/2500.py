import sys
input=sys.stdin.readline
n,k,t=map(int,input().split())
mod=42043
L=[]

def mul(L1, L2):
    res=[0]*(k+1)
    for i in range(k+1):
        for j in range(k+1):
            if i+j>k:continue
            res[i+j]+=L1[i]*L2[j]
            res[i+j]%=mod
    return res

def pow(L, n):
    if n==1:return L
    L1=pow(L,n//2)
    L2=L1[:]
    if n%2:return mul(mul(L1,L2), L)
    return mul(L1, L2)

for i in ' '*t:L.append(int(input()))

eq=[0]*(k+1)
for i in L:
    if i<=k:eq[i]+=1
res=pow(eq, n)
ans=0
for i in res:
    ans+=i
    ans%=mod
print(ans)