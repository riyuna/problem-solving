import sys
from collections import deque
from bisect import bisect_left
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

w,h=linput()
n=iinput()
L=[]
for i in ' '*n:L.append(linput())
a=iinput()
A=linput()
b=iinput()
B=linput()

mem=dict()
res=-1
ct=0
mn=10**10
for i1, i2 in L:
	aa=bisect_left(A, i1)
	bb=bisect_left(B, i2)
	if (aa,bb) not in mem:
		mem[(aa,bb)]=0
		ct+=1
	mem[(aa,bb)]+=1
	res=max(mem[(aa,bb)],res)

if ct<(a+1)*(b+1):mn=0
else:
	for k in mem:
		mn=min(mn, mem[k])
print(mn, res)