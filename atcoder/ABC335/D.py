import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
dir=[(1,0), (0,1), (-1, 0), (0,-1)]
d=dict()
for i in range(4):
	d[dir[i-1]]=dir[i]
L=[[None]*n for i in range(n)]
L[n//2][n//2]='T'
nowdir=(1,0)
nowx=0
nowy=0
for i in range(1, n**2):
	L[nowy][nowx]=i
	x,y=nowdir
	if 0<=nowx+x<n and 0<=nowy+y<n and L[nowy+y][nowx+x]==None:
		nowy+=y
		nowx+=x
		continue
	nowdir=d[nowdir]
	x,y=nowdir
	nowy+=y
	nowx+=x
for i in L:
	for j in i:print(j, end=' ')
	print()