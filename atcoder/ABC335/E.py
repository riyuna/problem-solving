import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,m=linput()
p=[-1]*(n+1)
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a
    
L=linput()
adj=dict()
for i in range(n):adj[i+1]=[]
for i in range(m):
	a,b=linput()
	a=find(a)
	b=find(b)
	if find(a)==find(b):continue
	if L[a-1]<L[b-1]:adj[a].append(b)
	if L[b-1]<L[a-1]:adj[b].append(a)
	if L[a-1]==L[b-1]:
		merge(a,b)
newadj=dict()
for i in range(1, n+1):
     k=find(i)
     if k not in newadj:newadj[k]=set()
     for j in adj[i]:newadj[k].add(j)

start=find(1)
end=find(n)
dp=[0]*(n+1)
dp[start]=1
q=deque()
q.append(start)
while len(q):
    k=q.popleft()
    for i in adj[k]:
        q.append(i)
        dp[i]=max(dp[i], dp[k]+1)
print(dp[end])