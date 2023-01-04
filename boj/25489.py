from collections import deque
from sys import stdin
input = stdin.readline
n=int(input())
L=list(map(float,input().split()))
d=dict()
for i in ' '*(n-1):
	a,b=map(int,input().split())
	if a-1 not in d:d[a-1]=dict()
	if b-1 not in d:d[b-1]=dict()
	d[a-1][b-1]=1
	d[b-1][a-1]=1
	
psum = sum(L)
childs = [[] for i in range(n)]
parent = [-1]*n
bfs = deque()

visited = [False]*n
ct=0
bfs.append(0)
while bfs:
	t = bfs.popleft()
	if not visited[t]:
		visited[t]=True
	for i in d[t]:
		if not visited[i]:
			bfs.append(i)
			childs[t].append(i)
			parent[i]=t

csum = [0]*n
for i in range(n):
	for j in childs[i]:
		csum[i]+=L[j]

edgesum = 0

def f(i):
	return L[i] * (len(childs[i]) - csum[i]) + (1-L[i]) * csum[i]

for i in range(n):
	edgesum += f(i)

print(psum+edgesum)

for _ in ' '*int(input()):
	u, p = input().split()
	u=int(u)-1
	p=float(p)
	prev = L[u]
	psum += (p-prev)
	bumo = parent[u]
	if bumo!=-1:
		edgesum -= f(bumo)
		edgesum -= f(u)
		L[u] = p
		csum[bumo] += (p-prev)
		edgesum += f(bumo)
		edgesum += f(u)
		print(psum+edgesum)
	else:
		edgesum -= f(u)
		L[u] = p
		edgesum += f(u)
		print(psum+edgesum)