n,k,c=map(int,input().split())
mod = 998244353
dp = [[0, 0] for i in range(n+1)]
dp[0]=[1,1]
if c==1:print(1)
else:
	if k==1 or k==2:print(pow(c, n, mod))
	else:
		for i in range(1, n+1):
			dp[i][1] = dp[max(0, i-k+2)][0]
			if i<=k-1:dp[i][1]=c
			dp[i][0] = dp[i-1][1] *(c-2) + dp[i-1][0]*2
			dp[i][1]%=mod
			dp[i][0]%=mod
		print(dp[-1][0])