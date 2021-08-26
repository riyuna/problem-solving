import sys
input = sys.stdin.readline

n,m,k,s,t=map(int,input().split())
adj = [dict() for i in range(n)]

for i in ' '*m:
    a,b,t1=map(int,input().split())
    adj[a-1][b-1] = t1
    adj[b-1][a-1] = 0

dp = [[-1]*(k+1) for i in range(n)]
dp[t-1][k] = 0
for j in range(k, -1, -1):
    for i in range(n-1, -1, -1):
        if i>t-1 and j==k:
            dp[i][j]=-10**15
            continue
        if i==t-1 and j==k:continue
        mx=-10**10
        if j!=k:mx=max(mx, dp[i][j+1])
        for kk in adj[i]:
            if kk<i:
                if j!=k:mx = max(mx, dp[kk][j+1])
            else:
                mx=max(mx, dp[kk][j]+adj[i][kk])
        dp[i][j]=mx

print(dp[s-1][0] if dp[s-1][0]>-1 else -1)