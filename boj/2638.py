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
for i in ' '*n:L.append(linput())


ct=0
while True:
    q=deque()
    q.append((0,0))
    visited=dict()
    mem=[]
    while len(q):

        x,y=q.popleft()
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            xx=x+dx
            yy=y+dy
            if 0<=xx<n and 0<=yy<m:
                if L[xx][yy]==0 and (xx,yy) not in visited:
                    visited[(xx,yy)]=True
                    q.append((xx,yy))
                if L[xx][yy]==1:
                    if (xx,yy) not in visited:
                        mem.append((xx,yy))
                        visited[(xx,yy)]=0
                    visited[(xx,yy)]+=1
    
    check=0
    for x,y in mem:
        if visited[(x,y)]>1:
            check=1
            L[x][y]=0
    if not check:break
    ct+=1
    
print(ct)