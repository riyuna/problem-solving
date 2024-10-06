import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,q=linput()
ryu=dict()
for i in range(1, n+1):
	ryu[i]=(i, 0)

pt=1
for _ in ' '*q:
	a,b=input().split()
	if a=='1':
		headx, heady=ryu[pt]
		if b=='R':headx+=1
		if b=='L':headx-=1
		if b=='U':heady+=1
		if b=='D':heady-=1
		ryu[pt-1]=(headx, heady)
		pt-=1
	else:
		b=int(b)
		x,y=ryu[b+pt-1]
		print(x,y)