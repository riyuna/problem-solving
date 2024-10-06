import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

s=input().strip()

res=0
for i in s:
	res*=26
	k=ord(i)-64
	res+=k

print(res)