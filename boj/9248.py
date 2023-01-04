import sys
from collections import deque
input = sys.stdin.readline
n,m,k=map(int,input().split())
cost = [[0]*2010 for i in range(2010)]
now = [[0]*2010 for i in range(2010)]

adj = dict()

for i in range(n):
	L = list(map(int,input().split()))
	for j in L[1:]:
		cost[i+1][j+n]=1
		# cost[j+n][i+1]=-1
		if i+1 not in adj:adj[i+1]=[]
		if j+n not in adj:adj[j+n]=[]
		adj[i+1].append(j+n)
		adj[j+n].append(i+1)
	cost[0][i+1]=1
	cost[n+m+2][i+1]=1
	# cost[i+1][0]=-1
	# cost[i+1][n+m+2]=-1
	if 0 not in adj:adj[0]=[]
	if i+1 not in adj:adj[i+1]=[]
	if n+m+2 not in adj:adj[n+m+2]=[]
	adj[0].append(i+1)
	adj[i+1].append(0)
	adj[n+m+2].append(i+1)
	adj[i+1].append(n+m+2)

adj[0].append(n+m+2)
adj[n+m+2].append(0)
cost[0][n+m+2]=k
# cost[n+m+2][0]=-k

for j in range(m):
	w = n+j+1
	sink = n+m+1
	cost[w][sink]=1
	# cost[sink][w]=-1
	if w not in adj:adj[w]=[]
	if sink not in adj:adj[sink]=[]
	adj[w].append(sink)
	adj[sink].append(w)
	


def flow(source, sink):
	res = 0
	while True:
		bfstree = [-1]*len(cost)
		q = deque()
		q.append(source)
		while q and bfstree[sink]==-1:
			k = q.popleft()
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

print(flow(0, n+m+1))