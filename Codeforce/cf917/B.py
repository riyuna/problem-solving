import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

for _ in ' '*iinput():
	n=iinput()
	s=input().strip()
	ctL=[0]*26
	ct=0
	for i in s:
		k=ord(i)
		ctL[k-97]+=1
		if ctL[k-97]==1:ct+=1
	result=0
	for i in range(n-1, -1, -1):
		result+=ct
		k=ord(s[i])-97
		if ctL[k]==1:
			ct-=1
		ctL[k]-=1
	print(result)