import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
    res=0
    n=int(input())
    for i in ' '*n:
        L=list(map(int,input().split()))+[0]
        res+=max(L)
    print(res)