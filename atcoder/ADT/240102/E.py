import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
s=bin(n)[2:]
for i in s:
	if i=='1':print(2,end='')
	else:print(0,end='')