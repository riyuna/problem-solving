import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
L=[[] for i in range(n)]
revL=[]
indeg=[0]*n
for i in range(n):
	M=linput()[1:]
	revL.append(M)
	indeg[i]=len(M)
	for j in M:
		L[j-1].append(i+1)

#connected with 1
q=deque([1])
visited=[False]*n
while len(q):
	k=q.pop()
	for i in revL[k-1]:
		if visited[i-1]==False:
			visited[i-1]=True
			q.append(i)

q=deque()
topo=[None]*n

for i in range(n):
	if indeg[i]==0:q.append(i+1)

state=True
for i in range(n):
	if len(q)==0:
		state=False
		break
	now=q.pop()
	topo[i]=now
	for j in L[now-1]:
		indeg[j-1]-=1
		if indeg[j-1]==0:q.append(j)

if not state:print(0)
for i in topo:
	if visited[i-1]:print(i,end=' ')