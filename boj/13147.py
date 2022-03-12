import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
dwarfs=set()
L=[]
for i in ' '*n:
	L.append(input().split())
	dwarfs.add(L[-1][0])
	dwarfs.add(L[-1][2])
d=dict()
ct=0
for dwarf in dwarfs:
	d[dwarf]=ct
	ct+=1
indeg=[0]*len(dwarfs)
adj=[[]for i in range(len(dwarfs))]

for line in L:
	a,b,c=line
	prev=0
	if b=='<':
		adj[d[a]].append(d[c]+1)
		indeg[d[c]]+=1
	else:
		adj[d[c]].append(d[a]+1)
		indeg[d[a]]+=1
n=len(dwarfs)
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
print('possible' if state else 'impossible')