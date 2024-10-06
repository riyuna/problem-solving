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
d=dict()
for i in range(n+m):
    a,b=linput()
    d[a]=b

q=deque()
q.append(1)
visited=[-1]*101
visited[1]=0
while True:
    k=q.popleft()
    for i in range(1, 7):
        a=k+i
        if a in d:a=d[a]
        if a>100:break
        if visited[a]==-1:
            visited[a]=visited[k]+1
            q.append(a)
        if a==100:break
    if a==100:break
print(visited[100])