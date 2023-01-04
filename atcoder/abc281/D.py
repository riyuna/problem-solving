import sys
input = sys.stdin.readline

n,K,d=map(int,input().split())
L=list(map(int,input().split()))
L.sort()

dp = [[[-1]*(d) for i in range(n+1)]for j in range(n+1)]
dp[0][0][0]=0
for i in range(1, n+1):
	for j in range(i+1):
		for k in range(d):
			if j==0:
				if k==0:
					dp[i][j][k]=0
				continue
			r=L[i-1]%d
			a = dp[i-1][j][k]
			b = dp[i-1][j-1][(k-r)%d]
			if a==b==-1:continue
			if b==-1:dp[i][j][k] = a
			elif a==-1:dp[i][j][k] = b+L[i-1]
			else:dp[i][j][k] = max(a, b+L[i-1])

# for i in dp:print(i)

print(dp[n][K][0])