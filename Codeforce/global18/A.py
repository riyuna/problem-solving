import sys
input=sys.stdin.readline

for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    print(1 if sum(L)%n else 0)