n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))

ptsum=[[0]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1, m+1):
        ptsum[i][j]=ptsum[i-1][j]+ptsum[i][j-1]-ptsum[i-1][j-1]+L[i-1][j-1]

def sweep(x, y):
    ct=0
    for i in range(n-y+1):
        for j in range(m-x+1):
            if ptsum[i+y][j+x]-ptsum[i][j+x]-ptsum[i+y][j]+ptsum[i][j]==10:ct+=1
    return ct

res=0
for i in range(1, 11):
    for j in range(1, 10//i+1):
        res+=sweep(i,j)
print(res)