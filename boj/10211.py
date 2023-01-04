import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	dp=[0]*n
	L=list(map(int,input().split()))
	res=0
	for j in range(n):
		dp[j] = max(L[j]+dp[j-1], dp[j])
		res=max(dp[j],res)
	print(res if max(L)>0 else max(L))