import sys
from math import gcd
input=sys.stdin.readline

for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    check=False
    for i in range(n):
        for j in range(i):
            if gcd(L[i], L[j])<3:check=True
    print('YNeos'[(1-check)::2])