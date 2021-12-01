import sys
input=sys.stdin.readline
from bisect import bisect_left
def solve(L):
    M=[]
    n=len(L)
    mem=[]
    nextL=[]
    pair=[[0,0]for i in range(n)]
    M.append(L[0])
    pair[0][0]=L[0]
    pair[0][1]=0
    pt=0
    for i in range(1, n):
        if M[pt]<=L[i]:
            M.append(L[i])
            pt+=1
            pair[i][0]=L[i]
            pair[i][1]=pt
        else:
            k=bisect_left(M, L[i])
            M[k]=L[i]
            pair[i][0]=L[i]
            pair[i][1]=k

    for i in range(n-1, -1, -1):
        if pair[i][1]==pt:
            mem.append(pair[i][0])
            pt-=1
        else:
            nextL.append(pair[i][0])
    return nextL
d=dict()
m,n,k=map(int,input().split())
for i in ' '*k:
    a,b=map(int,input().split())
    if a not in d:d[a]=[]
    d[a].append(b)
L=[]
for i in range(1, m+1):
    if i in d:
        d[i].sort()
        L.extend(d[i])

ct=0
while L:
    ct+=1
    L=solve(L)
print(ct)