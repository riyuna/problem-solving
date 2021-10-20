import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
    n,m=map(int,input().split())
    mem=dict()
    for i in ' '*m:
        a,b,c=map(int,input().split())
        mem[b]=True
    for i in range(1, n+1):
        if i not in mem:break
    for j in range(1, n+1):
        if i!=j:print(i, j)