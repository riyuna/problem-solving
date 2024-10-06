import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

for i in ' '*iinput():
	n=iinput()
	L=linput()
	ct0=False
	ctminus=0
	for i in L:
		if i<0:ctminus+=1
		if i==0:ct0=True
	if ct0:
		print(0)
		continue
	if ctminus%2==1:print(0)
	else:
		print(1)
		print(1, 0)