n,m=map(int,input().split())
mod=10**9+7
L=[[0]*m for i in range(n)]
L[0][0]=1
for i in range(n):
    for j in range(m):
        if i>0:L[i][j]+=L[i-1][j]
        if j>0:L[i][j]+=L[i][j-1]
        if i>0 and j>0:L[i][j]+=L[i-1][j-1]
        L[i][j]%=mod
print(L[-1][-1])