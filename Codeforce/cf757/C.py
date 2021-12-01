import sys
input=sys.stdin.readline
mod=10**9+7
for _ in ' '*int(input()):
    n,m=map(int,input().split())
    L=[]
    res=0
    for _ in ' '*m:
        l,r,x=map(int,input().split())
        res|=x
    res*=pow(2, n-1, mod)
    res%=mod
    print(res)