import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

for _ in ' '*int(input()):
	n,k,d=linput()
	L1=linput()
	L2=linput()
	check=[0]*4010
	if n==1:
		if L1[0]==0:print(d//2)
		elif L1[0]==1:print((d+1)//2)
		else:print((d-1)//2)
		continue

	if d==1:
		ct=0
		for i in range(n):
			if L1[i]==i+1:
				ct+=1
		print(ct)
		continue

	#dp[i]: 1 until i day and 2, 1, 2, 1, 2,...
	for i in range(n):
		if L1[i]==i+1:check[0]+=1
	check[0]+=(d-1)//2
	for i in range(1, min(2*n+1, d)):
		for j in range(L2[(i-1)%k]):
			L1[j]+=1
		for j in range(n):
			if L1[j]==j+1:
				check[i]+=1
		check[i]+=(d-i-1)//2
	print(max(check))