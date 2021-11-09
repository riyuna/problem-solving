from math import gcd
ans=0
mod=10**9+7
for i in ' '*int(input()):
    n,s=map(int,input().split())
    g=gcd(n,s)
    n//=g
    s//=g
    inv=pow(n, mod-2, mod)
    ans+=s*inv
    ans%=mod
print(ans)