import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

q,k=linput()

def mul(L1, n):
	#multiple x^n+1 to L1
	res=[0]*(min(len(L1)+n, k+1))
	for i in range(len(L1)):
		res[i]+=L1[i]
		res[i]%=mod
		if (i+n)<len(res):
			res[i+n]+=L1[i]
			res[i+n]%=mod
	return res

def div(L1, n):
	#divide x^n+1 to L1
	res=[0]*(len(L1))
	for i in range(len(L1)):
		res[i]=L1[i]
		res[i]%=mod
		if i+n<len(L1):L1[i+n]-=L1[i]
	return res

poly=[1]

for i in ' '*q:
	s,n=input().split()
	n=int(n)
	if s=='+':
		poly=mul(poly, n)
	else:
		poly=div(poly, n)
	ans=0
	if len(poly)>k:
		ans=poly[k]
	# print(poly)
	print(ans%mod)