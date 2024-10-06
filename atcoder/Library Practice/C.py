import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

from atcoder.math import floor_sum

for i in ' '*iinput():
	n,m,a,b=linput()
	print(floor_sum(n,m,a,b))