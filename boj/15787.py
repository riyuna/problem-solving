import sys
input=sys.stdin.readline
n,m=map(int,input().split())
L=[0]*n
for i in ' '*m:
    q=list(map(int,input().split()))
    if q[0]==1:
        L[q[1]-1]|= 1<<(q[2]-1)
    if q[0]==2:
        if L[q[1]-1] & 1<<(q[2]-1): L[q[1]-1] -= 1<<(q[2]-1)
    if q[0]==3:
        L[q[1]-1]*=2
        if L[q[1]-1]>=1<<20:L[q[1]-1]-=1<<20
    if q[0]==4:
        L[q[1]-1]//=2
print(len(set(L)))