n,m=map(int,input().split())
L=list(map(int,input().split()))
def checker(L, k):
	dp1=[0]*len(L)
	dp2=[0]*len(L)
	for i in range(k+1):
		dp1[i]=L[i]
		dp2[i]=L[i]
		if i and dp2[i]<dp2[i-1]:dp2[i]=dp2[i-1]
	for i in range(k+1,len(L)):
		dp1[i]=dp2[i-k-1]+L[i]
		dp2[i]=dp1[i]
		if dp2[i]<dp2[i-1]:dp2[i]=dp2[i-1]
	return dp2[-1]>=m

def solve(L, m):
	if max(L)>=m:return 'Free!'
	if sum(L)<m:return -1
	lo=0
	hi=len(L)-2
	while lo<hi:
		mid=(lo+hi+1)//2
		if checker(L, mid):
			lo=mid
		else:hi=mid-1
	return lo

print(solve(L,m))