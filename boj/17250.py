import sys
input=sys.stdin.readline
n,m=map(int,input().split())

p=[-1]*(n+1)
L=[0]
for i in ' '*n:L.append(int(input()))

def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return L[a]
    L[a],L[b]=L[a]+L[b], L[a]+L[b]
    p[b]=a
    return L[b]

for i in ' '*m:
    a,b=map(int,input().split())
    print(merge(a,b))