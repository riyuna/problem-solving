n,m,x=map(int,input().split())
L=list(map(int,input().split()))
L.sort()
cost=list(map(int,input().split()))
cost.sort(reverse=True)

def solve(k):
	ct = 0
	for i in range(k):
		ct+=max((L[k-i-1]-cost[i]),0)
	return ct<=x

lo=0
hi=min(n,m)
for i in range(50):
	mid = (lo+hi)//2
	if solve(mid):lo=mid
	else:hi=mid-1

print(hi if solve(hi) else lo)