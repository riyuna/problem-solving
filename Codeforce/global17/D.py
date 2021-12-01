n=int(input())
L=list(map(int,input().split()))
mod=10**9+7
d=dict()
mx=0
for i in L:
    ct=0
    while i%2==0:
        ct+=1
        i//=2
    if ct not in d:d[ct]=0
    d[ct]+=1
    mx=max(ct, mx)
res=0
for i in range(1, mx+1):
    if i in d:
        ct=0
        for j in range(i+1, mx+1):
            if j in d:ct+=d[j]
        res+=pow(2, d[i]+ct-1, mod)
        res%=mod
res=pow(2, n, mod)-res-1
res%=mod
print(res)