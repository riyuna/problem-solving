import sys
input=sys.stdin.readline

n,m=map(int,input().split())
adj=[dict() for i in range(n)]
visited=[False]*n
for i in ' '*m:
    a,b=map(int,input().split())
    adj[a-1][b-1]=True
    adj[b-1][a-1]=True

ct=n
p=[-1]*(n)
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    global ct
    a=find(a)
    b=find(b)
    if a==b:return
    if p[b]<0:
        ct-=1
    p[b]=a

q=[]
qres=[False]*n
for i in ' '*n:q.append(int(input()))
q=q[::-1]

for i in range(n):
    a=q[i]-1
    for b in adj[a]:
        if visited[b]==True:
            merge(a,b)
    visited[a]=True
    qres[n-i-1]=(ct==n-i)

for i in qres:
    print(['NO','YES'][i])