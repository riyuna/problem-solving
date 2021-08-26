n=int(input())
L=list(map(int,input().split()))
m=max(L)
dp=[[[0]*(m*2+1) for i in range(n+1)]for j in range(n)]
for j in range(n+1):
    for i in range(n):
        for k in range(2*m+1):
            if j==0:dp[i][j][k]=(k-m)
            elif k<=m:
                dp[i][j][k] = max(dp[(i+1)%n][j-1][k+L[i]], dp[i][j-1][k+L[(i+j-1)%n]])
            else:
                dp[i][j][k] = min(dp[(i+1)%n][j-1][k-L[i]], dp[i][j-1][k-L[(i+j-1)%n]])

mx=0
for i in dp:
    j=i[-1]
    if j[m]>mx:mx=j[m]

print((mx+sum(L))//2)