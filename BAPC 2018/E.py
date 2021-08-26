n=int(input())
L=list(map(int,input().split()))
L.sort()
mod=10**9+9
dp=[1]
rem=dict()
ct=0
fact=1
for i in range(n):
    if L[i] not in rem:
        rem[L[i]]=1
        ct+=1
        fact*=ct
    else:
        rem[L[i]]+=1
        ct+=1
        fact*=ct
        fact*=pow(rem[L[i]],mod-2,mod)
        fact%=mod
    res=0
    f = fact
    res = 0
    new_rem = rem.copy()
    for j in range(i+1):
        k=new_rem[L[j]]
        new_rem[L[j]]-=1
        f*=k
        f*=pow(i+1-j, mod-2, mod)
        f%=mod
        res+=f*dp[j]
    dp.append((fact-res)%mod)
print(dp[-1])