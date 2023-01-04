import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
pizza=list(map(int,input().split()))

indeg=[0]*n
adj=[[]for i in range(n)]
for i in ' '*m:
	L=list(map(int,input().split()))
	L[0]+=1
	L[1]+=1
	prev=0
	for j in L:
		if prev!=0:
			adj[prev-1].append(j)
			indeg[j-1]+=1
		prev=j
q=deque()
topo=[None]*n
for i in range(n):
	if indeg[i]==0:q.append(i+1)
state=True
for i in range(n):
	if len(q)==0:
		state=False
		break

	curr=q.pop()
	topo[i]=curr
	for j in adj[curr-1]:
		indeg[j-1]-=1
		if indeg[j-1]==0:q.append(j)

dp=[0]*n
for i in topo[::-1]:
	i-=1
	dp[i]=max(dp[i],pizza[i])
	for j in adj[i]:
		dp[i]=max(dp[i], dp[j-1]/2+pizza[i])
		dp[i]=max(dp[i], dp[j-1])
		
print(max(dp))