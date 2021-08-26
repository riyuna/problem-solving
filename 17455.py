import sys
from collections import deque

input = sys.stdin.readline
n,m=map(int,input().split())
s=input()
L=[]

indeg = [0]*n
adj = [[] for i in range(n)]

for i in ' '*m:
    a,b=map(int,input().split())
    a-=1
    b-=1
    if (s[a],s[b]) in (('K','D'), ('D','H'), ('H','K')):
        L.append((a,b))
        adj[a].append(b)
        indeg[b]+=1
    
    elif (s[b], s[a]) in (('K','D'), ('D','H'), ('H','K')):
        L.append((b,a))
        adj[b].append(a)
        indeg[a]+=1

q=deque()
topo=[None]*n
for i in range(n):
    if indeg[i]==0:q.append(i)
state=True
for i in range(n):
    if len(q)==0:
        state=False
        break

    curr=q.pop()
    topo[i]=curr
    for j in adj[curr]:
        indeg[j]-=1
        if indeg[j]==0:q.append(j)

if not state:print(-1)
else:
    d = dict()
    for i in range(n):
        d[topo[i]] = i
    dp=[1]*n
    for i in range(n-1, -1, -1):
        adj_list = adj[topo[i]]
        for j in adj_list:
            dp[i] = max(dp[d[j]]+1,dp[i])

    mx=-1
    for i in range(n):
        if s[topo[i]]=='K':mx=max(dp[i],mx)
    if mx<3:print(-1)
    else: print(mx//3*3)
