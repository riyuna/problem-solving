import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
#print('なんでや!阪神関係ないやろ!')

h,w=linput()
memred=[]
memgr=[]
def color(s):
    if s=='#':return 0
    else:return -1

L=[[-1]*(w+2)]+[[-1]+(list(map(color, list(input().strip()))))+[-1] for _ in range(h)]+[[-1]*(w+2)]

dir=[(1,0),(-1,0),(0,1),(0,-1)]
#find
ct=1
q=[]
r=[]
for i in range(1, h+1):
    for j in range(1, w+1):
        if L[i][j]==0:
            q.append((i,j))
        else:r.append((i,j))

for i, j in q:
    if L[i][j]!=0:continue
    qq=[(i,j)]
    while len(qq):
        newq=[]
        for ii, jj in qq:
            L[ii][jj]=ct
            for x,y in dir:
                if L[ii+x][jj+y]==0:
                    L[ii+x][jj+y]=ct  
                    newq.append((ii+x,jj+y))
        qq=newq
    ct+=1
component=ct-1
red=0
tot=0

for i,j in r:
    s=[-1]
    for x,y in dir:
        if L[i+x][j+y] not in s:s.append(L[i+x][j+y])
    c=component+2-len(s)
    red+=1
    tot+=c
print((tot*pow(red,mod-2,mod))%mod)