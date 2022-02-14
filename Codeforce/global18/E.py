import sys
from bisect import bisect_left

def lis(L):
    n=len(L)
    M=[]
    mem=[]
    pair=[[0,0]for i in range(n)]
    M.append(0)
    pair[0][0]=L[0]
    pair[0][1]=0
    pt=0
    rm=0
    for i in range(1, n):
        print(M)
        if M[pt]<=(L[i]-L[rm]):
            M.append(L[i]-L[rm])
            pt+=1
            pair[i][0]=L[i]
            pair[i][1]=pt
            rm=i
        else:
            k=bisect_left(M, L[i]-L[rm])
            M[k]=(L[i]-L[rm])
            pair[i][0]=L[i]-L[rm]
            pair[i][1]=k
    for i in range(n-1, -1, -1):
        if pair[i][1]==pt:
            mem.append(pair[i][0])
            pt-=1
    print(M)
    print(pair)
    print(mem)
    return len(mem)

for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()

    k=lis(L)
    print(n-k)