import sys
input=sys.stdin.readline
for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()
    for i in range(1, n//2+1):
        print(L[i], L[0])