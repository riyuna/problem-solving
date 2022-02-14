def checker(L):
    ct=0
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j]=='.':continue
            if i:
                ct+=L[i-1][j]=='o'
                if j:
                    ct+=L[i-1][j-1]=='o'
                if j+1!=len(L[i]):
                    ct+=L[i-1][j+1]=='o'
            if j:ct+=L[i][j-1]=='o'
            if i+1<len(L):
                ct+=L[i+1][j]=='o'
                if j+1<len(L[0]):
                    ct+=L[i+1][j+1]=='o'
            if j+1<len(L[0]):
                ct+=L[i][j+1]=='o'
                if i:
                    ct+=L[i-1][j+1]=='o'
    return ct//2

empty=[]
n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(list(input()))
for i in range(n):
    for j in range(m):
        if L[i][j]=='.':empty.append((i,j))

mx=checker(L)
for i, j in empty:
    newL=[]
    for ls in L:newL.append(ls[:])
    newL[i][j]='o'
    mx=max(checker(newL), mx)

print(mx)