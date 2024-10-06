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

n=iinput()
L=[]
shark=[-1,-1]
for i in range(n):
    L.append(linput())
    for j in range(n):
        if L[i][j]==9:shark=[i,j]

size=2
ct=0
def search(L, shark):
    global size
    global ct
    q=deque()
    q.append((shark[0],shark[1]))
    mem=[[-1]*n for i in range(n)]
    mem[shark[0]][shark[1]]=0
    dist=0
    fish=[]
    while len(q):
        newq=deque()
        dist+=1
        for x, y in q:
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                xx,yy=x+dx,y+dy
                if 0<=xx<n and 0<=yy<n:
                    if L[xx][yy]<=size and mem[xx][yy]==-1:
                        mem[xx][yy]=dist
                        newq.append((xx,yy))
                        if 0<L[xx][yy]<size:fish.append((dist,xx,yy))
        q=newq
    return fish
res=0
while True:
    fish=search(L, shark)
    fish.sort()
    if len(fish)==0:break
    d,x,y=fish[0]
    res+=d
    L[shark[0]][shark[1]]=0
    shark[0]=x
    shark[1]=y
    L[x][y]=9
    ct+=1
    if ct==size:
        ct=0
        size+=1
print(res)