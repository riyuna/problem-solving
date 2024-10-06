import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
for i in range(n+1):
	for j in range(n-i+1):
		for k in range(n-i-j+1):
			print(i,j,k)