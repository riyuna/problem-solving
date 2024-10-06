#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,m=linput()
L=[]
virus=deque()
empty=[]

for i in range(n):
    L.append(linput())
    for j in range(m):
        if L[i][j]==2:virus.append((i,j))
        if L[i][j]==0:empty.append((i,j))

def solve(L):
    visited=dict()
    for tup in virus:visited[tup]=True
    q=deque()
    for i in virus:q.append(i)
    while len(q):
        newq=deque()
        for x, y in q:
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                xx=x+dx
                yy=y+dy
                if 0<=xx<n and 0<=yy<m:
                    if (xx,yy) not in visited:
                        if L[xx][yy]==0:
                            newq.append((xx,yy))
                            visited[(xx,yy)]=True
                            L[xx][yy]=2
        q=newq
    res=0
    for i in range(n):
        for j in range(m):
            if L[i][j]==0:res+=1
    return res
res=0
for i in range(len(empty)):
    for j in range(i):
        for k in range(j):
            newL=[i[:] for i in L]
            newL[empty[i][0]][empty[i][1]]=1
            newL[empty[j][0]][empty[j][1]]=1
            newL[empty[k][0]][empty[k][1]]=1
            res=max(res, solve(newL))
print(res)