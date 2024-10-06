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
x,y=-1,-1
for i in range(n):
    s=input().strip()
    if 'I' in s:
        x,y=i,s.index('I')
    L.append(s)

visited=[[0]*m for i in range(n)]
q=deque()
q.append((x,y))
d=[[-1,0],[1,0],[0,1],[0,-1]]
res=0
while len(q):
    a,b=q.popleft()
    for dx, dy in d:
        x,y=a+dx,b+dy
        if 0<=x<n and 0<=y<m and not visited[x][y] and L[x][y]!='X':
            visited[x][y]=True
            q.append((x,y))
            if L[x][y]=='P':res+=1
if not res:print('TT')
else:print(res)