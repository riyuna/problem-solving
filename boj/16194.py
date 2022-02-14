n=int(input())
L=list(map(int,input().split()))
dp=[10**9]*(n+1)
dp[0]=0
for i in range(1, n+1):
	for j in range(i):
		dp[i]=min(dp[i], dp[i-j-1]+L[j])
print(dp[-1])