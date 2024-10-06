import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
dx=dict()
dy=dict()
dpt=dict()
pt=[]
for i in ' '*n:
	r,c,x=linput()
	if r not in dx:dx[r]=0
	dx[r]+=x
	if c not in dy:dy[c]=0
	dy[c]+=x
	dpt[(r,c)]=x
	pt.append((r,c))
ix=-1
iy=-1
memx=0
memy=0
for x in dx:
	if dx[x]>memx:
		memx=dx[x]
		ix=x
for y in dy:
	if dy[y]>memy:
		memy=dy[y]
		iy=y
res=0
for x in dx:
	k=dx[x]+memy
	if (x, iy) in dpt:k-=dpt[(x,iy)]
	res=max(res,k)
for y in dy:
	k=dy[y]+memx
	if (ix, y) in dpt:k-=dpt[(ix,y)]
	res=max(res,k)
print(res)