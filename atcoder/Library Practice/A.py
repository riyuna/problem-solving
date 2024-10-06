import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

from atcoder.dsu import DSU

n,q=linput()
union=DSU(n)

for _ in ' '*q:
	t,u,v=linput()
	if t==0:
		union.merge(u,v)
	else:
		print(int(union.same(u,v)))