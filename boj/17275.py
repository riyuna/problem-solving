import sys
input=sys.stdin.readline
t=int(input())
for _ in ' '*t:
    n,m=map(int,input().split())
    ct=[0]*n
    for _ in ' '*m:
        a,b=map(int,input().split())
        ct[a-1]+=1
        ct[b-1]+=1
    res=0
    for i in range(n):
        res+=ct[i]*(n-1-ct[i])
    print(n*(n-1)*(n-2)//6-res//2)