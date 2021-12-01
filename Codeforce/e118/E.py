import sys
from collections import deque
input=sys.stdin.readline
dir=[[-1,0], [1,0], [0,-1], [0, 1]]
for _ in ' '*int(input()):
    L=[]
    n,m=map(int,input().split())
    for i in ' '*n:
        L.append(list(input().strip()))
    #search L
    a,b=-1,-1
    for i in range(n):
        for j in range(m):
            if L[i][j]=='L':a,b=i,j
    
    #bfs
    q=deque([])
    q.append([a, b])
    visited=dict()
    visited[(a,b)]=True
    while len(q):
        a,b=q.popleft()
        cand=[]
        for x,y in dir:
            if 0<=a+x<n and 0<=b+y<m and (a+x, b+y) not in visited:
                cand.append([a+x,b+y])
        for x, y in cand:
            #check if candidate is valid or not
            ctother=0
            ctplus=0
            for dx, dy in dir:
                if 0<=x+dx<n and 0<=y+dy<m:
                    if L[x+dx][y+dy] in ('L', '+'):
                        ctplus+=1
                    if L[x+dx][y+dy]=='.':ctother+=1
            if ctother<2 and ctplus:
                if L[x][y]!='#':
                    L[x][y]='+'
                    q.append([x,y])
                    visited[(x,y)]=True
    for i in L:print(''.join(i))