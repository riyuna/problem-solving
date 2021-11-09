n=int(input())
mod=10**9+7
dp=[[0,0,0] for i in range(1600)]
dp[2][0]=1
dp[2][1]=1
for i in range(3, 1516):
    dp[i][0]=(dp[i-1][1]+dp[i-1][2])%mod
    dp[i][1]=(dp[i-1][0]+dp[i-1][2])%mod
    dp[i][2]=(dp[i-1][0]+dp[i-1][1])%mod

print(dp[n][0])