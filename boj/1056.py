import sys
from math import log
sys.setrecursionlimit(1000)
d=dict()
d[1]=0
d[2]=1
rem=dict()

def bnsearch(a,b,r):
    l=0
    while l<=r:
        mid=(l+r)//2
        if pow(mid, b)>=a: r=mid-1
        else: l=mid+1
    return l

def lim(k):
    l=2
    r=10**18
    while l<=r:
        mid=(l+r)//2
        if k*log(mid)<=log(10**18):
            l=mid+1
        else:r=mid-1
    return r

def solve(n):
    if n==1:return 0
    if n in d and d[n]:return d[n]
    ans=n-1
    for i in range(63, 1, -1):
        r=bnsearch(n,i,rem[i])
        l=r-1
        if r>1: ans=min(ans, solve(r)+abs(n-pow(r,i))+1)
        if l>1: ans=min(ans, solve(l)+abs(n-pow(l,i))+1)
    d[n]=ans
    return ans

for i in range(2, 64):
    rem[i]=lim(i)

n=int(input())
print(solve(n))