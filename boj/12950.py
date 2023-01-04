import sys
input = sys.stdin.readline
mx = 1e9
n,m=map(int,input().split())
adj = [[0]*n for i in range(n)]
for i in ' '*m:
	a,b,c=input().split()
	a=int(a)
	b=int(b)
	adj[a][b]=c
	adj[b][a]=c

dp=[[mx]*n for i in range(n)]

for i in range(n):
	dp[i][i]=0
for i in range(n):
	for j in range(n):
		if adj[i][j]!=0:
			dp[i][j]=1
			dp[j][i]=1


for t in range(2*n):
	for i in range(n):
		for j in range(n):
			if dp[i][j]!=mx:continue
			for k in range(n):
				for s in range(n):
					if adj[i][k] == adj[j][s] and adj[i][k]!=0:
						if dp[k][s]!=mx:
							dp[i][j]=dp[k][s]+2
							dp[j][i]=dp[k][s]+2

print(dp[0][1] if dp[0][1]!=mx else -1)