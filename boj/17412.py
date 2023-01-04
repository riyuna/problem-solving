import sys
from collections import deque
input = sys.stdin.readline
n,p=map(int,input().split())
cost = [[0]*410 for i in range(410)]
now = [[0]*410 for i in range(410)]

adj = dict()

for i in range(p):
	a,b=map(int,input().split())
	cost[a][b]+=1
	if a not in adj:adj[a]=[]
	if b not in adj:adj[b]=[]
	adj[a].append(b)
	adj[b].append(a)


def flow(source, sink):
	res = 0
	while True:
		bfstree = [-1]*len(cost)
		q = deque()
		q.append(source)
		while q and bfstree[sink]==-1:
			k = q.popleft()
			if k not in adj:continue
			for a in adj[k]:
				if cost[k][a] > now[k][a] and bfstree[a]==-1:
					q.append(a)
					bfstree[a]=k
					if a==sink:break
		
		if bfstree[sink] == -1:break
		mn = 1e18
		i = sink
		while i!=source:
			j=bfstree[i]
			mn = min(mn, cost[j][i] - now[j][i])
			i=j
		
		i = sink
		while i!=source:
			j=bfstree[i]
			now[j][i]+=mn
			now[i][j]-=mn
			i=j
		res+=mn

	return res

print(flow(1, 2))