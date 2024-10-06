import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

for i in ' '*(iinput()):
	n=iinput()
	print(['Bye', 'Good'][(n+1)%(n%100)==0])