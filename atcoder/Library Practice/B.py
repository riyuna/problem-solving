import sys
from collections import deque
from atcoder.segtree import SegTree
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

from atcoder.fenwicktree import FenwickTree

n,q=linput()
fenwick=FenwickTree(n)
L=linput()
for i in range(n):
	fenwick.add(i, L[i])

for _ in ' '*q:
	t,l,r=linput()
	if t==0:
		fenwick.add(l, r)
	else:
		print(fenwick.sum(l,r))