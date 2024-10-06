n,m=map(int,input().split())
L=list(map(int,input().split()))
mod=10**9+7
res=0
k=n+m-1
for i in range(m):
	t=pow(L[i], k, mod)
	for j in range(m):
		if i==j:continue
		a1,a2=L[i],L[j]
		t*=pow((a1-a2),mod-2, mod)
		t%=mod
	res+=t
	res%=mod
print(res)