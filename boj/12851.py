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
visited=[0]*100001
ct=0
mem=10**10
q=deque()
q.append((n, 0))
while q:
    now, dist = q.popleft()
    visited[now]=True
    if now == m:
        if dist<mem:
            mem=dist
            ct=0
        if dist==mem:
            ct+=1
    for next in [now-1, now+1, now*2]:
        if 0<=next<=100000 and not visited[next]:
            if dist<mem:q.append((next, dist+1))
print(mem)
print(ct)