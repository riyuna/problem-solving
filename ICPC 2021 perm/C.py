n=int(input())
L=list()
for i in ' '*n:
    M=list(input().split())
    M[1]=int(M[1])
    L.append(M)

M=[0]*n
res=0

for i in range(n-1, -1 ,-1):
    k=0
    if L[i][0]=='G':
        M[i]+=1
        for j in range(i): M[j]+=2**(i-j-(1-k))
    elif L[i][0]=='B':
        if M[i]%2==0 and L[i][1]!=1:
            if not i:res-=1
        else:k=1
        M[i]+=(2-k)
        for j in range(i): M[j]+=2**(i-j-k)

    else:
        if M[i]%2 and L[i][1]!=1:
            if not i:res-=1
            k=1
        M[i]+=(k+1)
        for j in range(i): M[j]+=2**(i-j-(1-k))

for i in range(n):
    res+=L[i][1]*M[i]

print(res)