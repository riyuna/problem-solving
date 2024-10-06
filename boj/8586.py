n=int(input())
L=list(map(int,input().split()))
sL=[0]
k=sum(L)
for i in L:sL.append(sL[-1]+i)
res=10**10
for i in range(n+1):
	a=(abs(i-sL[i])+abs(k-sL[i]))
	res=min(res, a)
print(res)