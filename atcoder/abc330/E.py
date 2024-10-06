import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

from atcoder.segtree import SegTree

mx=10**10
n,q=linput()
L=linput()
ct=[0]*(n+1)
for i in L:
	if i<n+1:ct[i]+=1
sg=SegTree(min, mx, ct)
for _ in ' '*q:
	p,x=linput()
	k=L[p-1]
	if k<=n:
		sg.set(k, sg.get(k)-1)
	L[p-1]=x
	if x<=n:
		sg.set(x, sg.get(x)+1)
	
	print(sg.max_right(0, lambda k:k>0))