n,k=map(int,input().split())
dp=[0]*k
for i in range(k):
	if i==0:
		dp[i]=(n+1)/2
		continue
	prev=dp[i-1]
	dp[i]=((n-int(prev))*(n+int(prev)+1)/2+int(prev)*prev)/n

print(dp[-1])