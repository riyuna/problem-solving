dp=[[0]*51 for i in range(1001)]

for i in range(1, 1001):
    dp[i][1]=i
for i in range(1, 1001):
    for j in range(2, 51):
        dp[i][j]=10**10
        for k in range(1, i+1):
            dp[i][j]=min(dp[i][j], max(dp[k-1][j-1], dp[i-k][j])+1)

for _ in ' '*int(input()):
    n,m=map(int,input().split())
    print(dp[m][n])