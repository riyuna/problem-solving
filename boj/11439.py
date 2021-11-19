n,k,m=map(int,input().split())
pL=[]
L=[True]*(4000001)
L[0]=False
L[1]=False
for i in range(2, 4000001):
    if not L[i]: continue
    pL.append(i)
    for j in range(2*i, 4000001, i):
        L[j]=False

d=dict()
for p in pL:
    j=p
    rem=0
    while j<=n:
        rem+=(n//j-(n-k)//j-k//j)
        j*=p
    if rem:d[p]=rem

res=1
for p in d:
    res*=pow(p, d[p], m)
    res%=m

print(res)