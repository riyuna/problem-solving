import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,m=linput()
L1=[]
L2=[]
for i in ' '*n:
	L1.append(input().strip())
for i in ' '*n:
	L2.append(input().strip())

state=False
for i in range(n):
	for j in range(m):
		flag=True
		for k in range(n):
			for s in range(m):
				if L1[(i+k)%n][(j+s)%m]!=L2[k][s]:
					flag=False
					continue
		if flag:state=True
print('YNeos'[(1-state)::2])