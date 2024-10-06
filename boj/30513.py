m,n=map(int,input().split())
mod=10**9+7
fact=[1]
for i in range(200000):
	fact.append((fact[-1]*(i+1))%mod)
revfact=[0]*200001
revfact[-1]=pow(fact[-1],mod-2, mod)
for i in range(199999, -1 , -1):
	revfact[i]=(revfact[i+1]*(i+1))%mod
def comb(n,k):
	return (fact[n]*revfact[k]*revfact[n-k])%mod
res=comb(n+m, m+1)
while n>=m:
	res+=comb(n,m)
	n-=m
print(res%mod)