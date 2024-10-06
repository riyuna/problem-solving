import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,a,b=linput()
L=linput()
print(L.index(a+b)+1)