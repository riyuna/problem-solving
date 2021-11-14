n=int(input())
mod=10**9+7
dp=[[0,0] for i in range(n+1)]
if n==1:print(2)
elif n==2:print(7)
else:
    dp[1][0]=2
    dp[2][0]=7
    dp[2][1]=1
    for i in range(3, n+1):
        dp[i][1]=dp[i-3][0]+dp[i-1][1]
        dp[i][1]%=mod
        dp[i][0]=dp[i][1]*2+dp[i-1][0]*2+dp[i-2][0]*3
        dp[i][0]%=mod
    print(dp[n][0])