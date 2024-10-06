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

import heapq
import math
MAX=math.inf
v,e=map(int,input().split())
L=[[]for i in range(v)]
for i in ' '*e:
    a,b,c=map(int,sys.stdin.readline().split())
    L[a-1].append((b,c))
    L[b-1].append((a,c))
v1,v2=linput()
def solve(k):
	dist=[]
	distm=[MAX]*v
	distm[k-1]=0
	heapq.heappush(dist,(0,k))
	while True:
		if len(dist)==0:break
		a=heapq.heappop(dist)
		if a[0]>distm[a[1]-1]:continue
		else:
			for i in L[a[1]-1]:
				if i[1]+distm[a[1]-1]<distm[i[0]-1]:
					distm[i[0]-1]=i[1]+distm[a[1]-1]
					heapq.heappush(dist,(i[1]+distm[a[1]-1],i[0]))
	return distm
a=solve(1)[v1-1]+solve(v1)[v2-1]+solve(v2)[v-1]
b=solve(1)[v2-1]+solve(v2)[v1-1]+solve(v1)[v-1]
res=min(a,b)
if res==MAX:print(-1)
else:print(res)