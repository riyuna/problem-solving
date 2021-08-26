import collections
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
check=[[False]*m for i in range(n)]
L=[]
for i in ' '*n:
    L.append(list(map(int,input().split())))
M = []
for i in ' '*n:
    M.append(list(map(int,input().split())))

dir=[[1,0],[-1,0],[0,1],[0,-1]]
q=collections.deque()
breaked = False
prep = -1
post = -1
for i in range(n):
    for j in range(m):
        if L[i][j]!=M[i][j]:
            q.append([j,i])
            check[i][j]=True
            prep = L[i][j]
            post = M[i][j]
            breaked=True
            break
    if breaked:break

if prep == post == -1:print('YES')
else:
    while len(q):
        a=q.popleft()
        x=a[0]
        y=a[1]
        for i in dir:
            nx=x+i[0]
            ny=y+i[1]
            if 0<=nx<m and 0<=ny<n and check[ny][nx]==False and L[ny][nx]==prep:
                check[ny][nx]=True
                q.append([nx,ny])
    
    res = True
    breaked = False
    for i in range(n):
        for j in range(m):
            if (check[i][j] and M[i][j]==post) or (not check[i][j] and M[i][j]==L[i][j]): continue
            else: 
                res=False
                breaked=True
                break
        if breaked:break
    if res:print('YES')
    else:print('NO')