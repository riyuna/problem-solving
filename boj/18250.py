import sys
input = sys.stdin.readline
n,m=map(int,input().split())

odd = [0]*n
parent = []
component = [1]*n

degree = [0]*n
pairs = []

for i in range(n):parent.append(i)

def find(k):
    if k==parent[k]: return k
    parent[k] = find(parent[k])
    return parent[k]

def merge(a, b):
    a=find(a)
    b=find(b)
    if a!=b:
        parent[b]=a
        odd[a]+=odd[b]
        component[a]+=component[b]

for i in ' '*m:
    a,b=map(int,input().split())
    pairs.append((a-1,b-1))
    degree[a-1]+=1
    degree[b-1]+=1

for i in range(n):
    odd[i]=degree[i]%2

for a,b in pairs:
    merge(a,b)

ans=0

for i in range(n):
    k=find(i)
    if i==k and component[i]>1:
        od_pt = odd[i]
        if od_pt==0:ans+=1
        else: ans+=od_pt//2

print(ans)