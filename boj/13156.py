c,m=map(int,input().split())
L=[]
for i in ' '*m:L.append([0]+list(map(int,input().split())))
dp=[[0]*(c+1) for i in range(m+1)]
for i in range(1, m+1):
	for j in range(c+1):
		for k in range(j, c+1):
			dp[i][j]=max(dp[i][j], dp[i-1][k]+L[i-1][k-j])

print(max(dp[-1]))