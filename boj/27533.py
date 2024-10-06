n,m=map(int,input().split())
mod = int(1e9+7)
fact=[1]
for i in range(810000):
    fact.append(fact[-1]*(i+1)%mod)
def c(n):
    res=fact[2*n]
    res*=(pow(fact[n], mod-2, mod)**2)%mod
    res*=pow(n+1, mod-2, mod)
    res%=mod
    return res

def solve(n, m):
    if n==m==2:return 2
    res=0
    if n>m:n,m=m,n
    for i in range(n-1):
        a=n-2-i
        b=m-2-i
        ct=fact[n+m-4]*pow(fact[a], mod-2, mod)*pow(fact[b], mod-2, mod)*pow(fact[i*2], mod-2, mod)
        ct%=mod
        res+=ct*c(i)
        res%=mod
    return res*2%mod

print(solve(n,m))