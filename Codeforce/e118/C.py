import sys
input=sys.stdin.readline
def check(L, h, k):
    ct=0
    for i in range(len(L)-1):
        ct+=min(L[i+1]-L[i], k)
    ct+=k
    return ct>=h
for _ in ' '*int(input()):
    n,h=map(int,input().split())
    L=list(map(int,input().split()))
    lo=1
    hi=10**18
    while lo<hi:
        mid=(lo+hi)//2
        res=check(L,h,mid)
        # print(mid, res)
        if res:
            hi=mid
        else:
            lo=mid+1
    print(lo)