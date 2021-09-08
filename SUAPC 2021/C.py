n,m=map(int,input().split())
dp=[[0]*m for i in range(n)]
L=[]
for i in ' '*n:L.append(input())
ct=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0: dp[i][j]=1
        elif L[i][j]==L[i-1][j-1] and L[i][j]!=L[i-1][j] and L[i-1][j]==L[i][j-1]:
            dp[i][j]=min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]])+1
        else: dp[i][j]=1
        ct+=dp[i][j]
print(ct)