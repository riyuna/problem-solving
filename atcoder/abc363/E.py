#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
from math import inf
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
import heapq
put = heapq.heappush
pop = heapq.heappop

q=[]
h,w,yyy=linput()
L=[]
for i in range(h):L.append(linput())
for i in range(h):
    put(q, (0, (i, -1)))
    put(q, (0, (i, w)))
for i in range(w):
    put(q, (0, (-1, i)))
    put(q, (0, (h, i)))

dp=[[inf]*w for i in range(h)]
dr=[[-1,0],[1,0],[0,1],[0,-1]]
while len(q):
    level, tup = pop(q)
    x,y=tup
    for dx, dy in dr:
        xx=x+dx
        yy=y+dy
        if 0<=xx<h and 0<=yy<w:
            val=min(max(L[xx][yy], level), dp[xx][yy])
            if val<dp[xx][yy]:
                dp[xx][yy]=val
                put(q, (val, (xx, yy)))
mem=dict()
for i in dp:
    for j in i:
        if j not in mem:mem[j]=0
        mem[j]+=1
res=h*w
for i in range(1, yyy+1):
    if i in mem:res-=mem[i]
    print(res)