import sys
input = sys.stdin.readline
h,w=map(int,input().split())
grid = []
for i in ' '*h:grid.append(input().strip())
mod = 998244353
L=[[[0, 0, 0]for i in range(w)]for j in range(h)]
L[0][0][0]=1
for i in range(h):
    for j in range(w):
        if i>0:
            a,b,c = L[i-1][j]
            if grid[i][j]==grid[i-1][j]=='Y':
                b+=a
                c+=2*b-a
            L[i][j][0]+=a
            L[i][j][1]+=b
            L[i][j][2]+=c
        if j>0:
            a,b,c=L[i][j-1]
            if grid[i][j]==grid[i][j-1]=='Y':
                b+=a
                c+=2*b-a
            L[i][j][0]+=a
            L[i][j][1]+=b
            L[i][j][2]+=c
        L[i][j][0]%=mod
        L[i][j][1]%=mod
        L[i][j][2]%=mod

print(L[-1][-1][-1])