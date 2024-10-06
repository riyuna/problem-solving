import sys
from atcoder.segtree import SegTree
input = sys.stdin.readline
def linput():return list(map(int,input().split()))

n,q=linput()
L=linput()
sg=SegTree(max, -1, L)
for _ in ' '*q:
	t,a,b=linput()
	if t==1:
		sg.set(a-1, b)
	elif t==2: 
		print(sg.prod(a-1, b))
	else:
		print(sg.max_right(a-1, lambda k:k<b)+1)
