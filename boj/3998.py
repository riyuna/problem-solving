remd=dict()
p=9705276
q=12805858
for i in range(1, 401):
    for j in range(i+1):
        remd[(i-j)*p+j*q]=(i-j, j)

L=[]
mxk=0
for i in ' '*int(input()):
    k=float(input())
    k*=100000
    k=int(k)
    mxk=max(mxk, k)
    if k in remd:L.append(remd[k])

mxa,mxb=remd[mxk]
newL=[]
for a,b in L:
    if a<=mxa and b<=mxb:newL.append((a,b))

M=[[0]*(mxb+1) for i in range(mxa+1)]
for a,b in newL:
    M[a][b]=1
    M[mxa-a][mxb-b]=1

dp=[[0]*(mxb+1) for i in range(mxa+1)]

for i in range(mxa+1):
    for j in range(mxb+1):
        if i:dp[i][j]=max(dp[i][j], dp[i-1][j])
        if j:dp[i][j]=max(dp[i][j], dp[i][j-1])
        dp[i][j]+=M[i][j]

for i in dp:print(i)