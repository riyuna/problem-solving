n=int(input())
L=[]
ans=10**10
for i in ' '*n:L.append(list(map(int,input().split())))
for i in range(3):
    dp=[[0,0,0]for i in range(n)]
    dp[0]=[10**10]*3
    dp[0][i]=L[0][i]
    for j in range(1, n):
        dp[j][0]=min(dp[j-1][1], dp[j-1][2])+L[j][0]
        dp[j][1]=min(dp[j-1][0], dp[j-1][2])+L[j][1]
        dp[j][2]=min(dp[j-1][0], dp[j-1][1])+L[j][2]
    dp[n-1][i]=10**10
    ans=min(ans, min(dp[n-1]))
print(ans)