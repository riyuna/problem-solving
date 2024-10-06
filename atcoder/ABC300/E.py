import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
k=pow(5, mod-2, mod)
mem=dict()
def f(n):
	if n in mem:return mem[n]
	if n==1:return 1
	if n in [2,3,5]:
		mem[n]=k
		return mem[n]
	res=0
	for i in range(2,7):
		if n%i==0:
			res+=(f(n//i)*k)%mod
			res%=mod
	mem[n]=res
	return res
print(f(iinput()))