n,k=map(int,input().split())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))
res=[]
for i in range(n):
    for _ in range(k):
        M=[]
        for j in L[i]:
            for _ in range(k):M.append(j)
        res.append(M)
for i in range(k*n):
    for j in range(k*n):
        print(res[i][j],end=' ')
    print()