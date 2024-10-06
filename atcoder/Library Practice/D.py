import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

from atcoder.maxflow import MFGraph

n,m=linput()
s=n*m
t=s+1
g=MFGraph(t+1)
grid = []
for _ in ' '*n:grid.append(list(input().strip()))

for i in range(n):
	for j in range(m):
		if grid[i][j]=='#':continue
		if (i+j)%2:
			g.add_edge(i*m+j, t, 1)
		else:
			g.add_edge(s, i*m+j, 1)

dir = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(n):
	for j in range(m):
		if (i+j)%2:continue
		if grid[i][j]=='#':continue
		for dx, dy in dir:
			ii=i+dx
			jj=j+dy
			if 0<=ii<n and 0<=jj<m and grid[ii][jj]=='.':
				g.add_edge(i*m+j, ii*m+jj, 1)

print(g.flow(s, t))

for e in g.edges():
	if e.src == s or e.dst == t or e.flow == 0:continue
	(i,j)=e.src//m, e.src%m
	(ii,jj)=e.dst//m, e.dst%m

	if i==ii+1:
		grid[ii][jj]='v'
		grid[i][j]='^'
	
	if j==jj+1:
		grid[ii][jj]='>'
		grid[i][j]='<'

	if i==ii-1:
		grid[ii][jj]='^'
		grid[i][j]='v'
	
	if j==jj-1:
		grid[ii][jj]='<'
		grid[i][j]='>'

for r in grid:
	print(''.join(r))