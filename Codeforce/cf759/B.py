import sys
input=sys.stdin.readline

for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    mx=max(L)
    pt=n-1
    ct=0
    while L[pt]!=mx:
        c=L[pt]
        while L[pt]<=c:
            pt-=1
        ct+=1
    print(ct)