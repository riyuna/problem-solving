from math import gcd
n,m=map(int,input().split())
dp = [[0]*21 for i in range(21)]
dp[0][0]=1

for i in range(1, 21):
	for j in range(1, i+1):
		dp[i][j] += dp[i-1][j] * (i-1) + dp[i-1][j-1]
	
div=1
for i in range(1, n+1):div*=i
res=0
for i in range(1, m+1):res+=dp[n][i]
g = gcd(div, res)
print(f"{res//g}/{div//g}")