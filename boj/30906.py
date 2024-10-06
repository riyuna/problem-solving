import sys
from collections import defaultdict as dd
input=sys.stdin.readline
n=int(input())
d=dd(int)
for i in ' '*n:
    x,y,z,w=map(int,input().split())
    d[(x,y)]+=1
    d[(z,w)]+=1
flag=False
for i in d:flag|=(d[i]%2)
print('yneos'[1-flag::2])