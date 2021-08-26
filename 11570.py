n=int(input())
L=list(map(int,input().split()))

dp=[[10**9]*(n+1) for i in range(n+1)]
dp[1][0]=0
dp[0][1]=0
for i in range(n):
    for j in range(n):
        if i==j:continue
        k=max(i,j)+1
        kj = dp[i][j]+abs(L[k-1]-L[i-1]) if i else dp[i][j]
        ik = dp[i][j]+abs(L[k-1]-L[j-1]) if j else dp[i][j]
        dp[k][j]=min(dp[k][j], kj)
        dp[i][k]=min(dp[i][k], ik)

print(min(dp[-1]))