L=[]
n,m=map(int,input().split())
for i in ' '*n:L.append(input())
c=0
r=0
for i in range(n):
    if L[i]=='.'*m:c+=1
for i in range(m):
    state=True
    for j in range(n):
        if L[j][i]!='.':
            state=False
            break
    if state:r+=1

print(c+r-min(c,r))