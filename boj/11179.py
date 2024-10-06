#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os, heapq
from math import inf
from collections import deque
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

v=iinput()
e=iinput()
adj=[[]for i in range(v)]
for i in ' '*e:
    a,b,c=linput()
    adj[a-1].append((b-1,c))
dist=[inf]*v
s,e=linput()
s-=1
e-=1

heap=[]
heapq.heappush(heap, [0, s, [s]])
dist[s]=0

while len(heap):
    d,i,L=heapq.heappop(heap)
    if i==e:
        print(dist[e])
        print(len(L))
        for i in L:print(i+1,end=' ')
        break
    for a,b in adj[i]:
        if dist[a]>d+b:
            dist[a]=(d+b)
            heapq.heappush(heap, [d+b, a, L+[a]])
#     print(heap)
# print(dist)
# print(adj)
