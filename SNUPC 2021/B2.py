L=[]
n,m=map(int,input().split())
for i in ' '*3*n:L.append(list(input()))
for i in range(n):
    for j in range(m):
        if (i+j)%2==0:continue
        state=False
        if i and L[i*3-1][j*3+1]=='#':
            state=True
            L[i*3][j*3+1]='#'
        if i!=n-1 and L[i*3+3][j*3+1]=='#':
            state=True
            L[i*3+2][j*3+1]='#'
        if j and L[i*3+1][j*3-1]=='#':
            state=True
            L[i*3+1][j*3]='#'
        if j!=m-1 and L[i*3+1][j*3+3]=='#':
            state=True
            L[i*3+1][j*3+2]='#'
        if state:L[i*3+1][j*3+1]='#'

for i in L:print(''.join(i))