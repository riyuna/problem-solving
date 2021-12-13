import sys
input=sys.stdin.readline

def solve(L, k):
    n=len(L)
    if n==0:return 0
    r=n%k
    if r==0:r=k
    res1=0
    res2=0
    for i in range(0, n, k):
        a,b=L[i],L[min(i+k-1, n-1)]
        if a*b<0:
            res1+=2*(abs(a)+abs(b))
        else:
            res1+=2*max(abs(a), abs(b))
    
    for i in range(r-k, n, k):
        a,b=L[max(i, 0)], L[i+k-1]
        if a*b<0:
            res2+=2*(abs(a)+abs(b))
        else:
            res2+=2*max(abs(a), abs(b))
    return min(res1, res2)

for _ in ' '*int(input()):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    L.sort()
    L1=[]
    L2=[]
    for i in L:
        if i<0:L1.append(i)
        elif i>0:L2.append(i)
        else:continue
    res=solve(L1,k)+solve(L2,k)
    res-=max(abs(L[0]), abs(L[-1]))
    print(res)