n=int(input())
check=[[0]*100 for i in range(100)]
dp=[[0]*100 for i in range(100)]
for i in ' '*n:
    i,j=map(int,input().split())
    check[i-1][j-1]=1
    check[j-1][i-1]=1

for j in range(100):
    for i in range(j, -1, -1):
        for k in range(i, j):
            dp[i][j]=max(dp[i][j], dp[i][k]+dp[k][j]+check[i][j])

print(dp[0][99])