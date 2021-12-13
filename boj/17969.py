import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
L=[dict() for i in range(n)]
dist=[]
sz=[0]*n
deg=[0]*n

for i in ' '*(n-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    deg[a]+=1
    deg[b]+=1
    L[a][(b, c)]=True
    L[b][(a, c)]=True

def size(pt, sub=-1):
    sz[pt]=1
    for i,j in L[pt]:
        if i!=sub: sz[pt]+=size(i, pt)
    return sz[pt]

def cent(pt, sub=-1):
    tree_size=size(pt)
    for i,j in L[pt]:
        if i!=sub and sz[i]*2>tree_size: return cent(i, pt)
    return pt

def distance(pt, sub, w):
    global dist
    for i,j in L[pt]:
        if i==sub:continue
        dist=distance(i, pt, w+j)
    if deg[pt]==1: dist.append(w)
    return dist

def solve(pt):
    global dist
    if deg[pt]==1:return 0
    perm=[]
    sm=[]
    sm2=[]
    for i,j in L[pt]:
        dist=[]
        distance(i, pt, j)
        perm.append(dist[:])
        s1=0
        s2=0
        for k in dist:
            s1+=k
            s2+=k**2
        sm.append(s1)
        sm2.append(s2)
    res=0
    for i in range(len(perm)):
        for j in range(i):
            res+=sm2[i]*len(perm[j])+2*sm[i]*sm[j]+sm2[j]*len(perm[i])
    return res

q=deque([])
q.append(0)
res=0
while len(q):
    k=q.popleft()
    c=cent(k)
    a=solve(c)
    res+=a
    for i,j in L[c]:
        del(L[i][(c, j)])
        q.append(i)
    L[c]=dict()

print(res)