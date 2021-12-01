import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    ct=0
    for i in range(n):
        while L[i]%2==0:
            ct+=1
            L[i]//=2
    mx=max(L)
    s=sum(L)-mx
    print(s+mx*pow(2,ct))